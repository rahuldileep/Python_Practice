# Requirements:

# 1. Any library member should be able to search for the book by their title, author, and catogory. 
# 2. Any library member should be able to checkout a book.
# 3. Any library member should be able to reserve a book for the future date if not available today.
# 4. Any library member should be able to return the book.
# 5. System should be able to retrieve info on any book. 
# 6. System should send notification for the reserve/reminder/extra fine etc.
# 7. Each member and a book will have unique barcodes. 
# 8. A book will have multiple copies and each copy should have a UIN.
# 9. Each book item should have a location in the library. 
# 10. There should be a limit on books and number of days. 


# There are 3 actors here - User/Librarian/System


# Account, Member, Librarian: These are the classes that interact with the system
# BookReservation, BookLending, and Fine: These classes represent a book reservation, lending, and fine collection, respectively.
# Book, BookItem, Rack - Responsible for processing the reservation, return and renewal
# Search interface and Catalog: The Catalog class will implement the Search interface to facilitate searching of books.

from abc import ABC, abstractmethod
from enum import Enum

class BookStatus(Enum):
  AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4


class ReservationStatus(Enum):
  WAITING, PENDING, CANCELED, COMPLETED, RESERVED = 1, 2, 3, 4, 5


class AccountStatus(Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5

class Constants:
  self.MAX_BOOKS_ISSUED_TO_A_USER = 5
  self.MAX_LENDING_DAYS = 10

class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country

class Person(ABC):
  def __init__(self, name, address, email, phone):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone

class Account(ABC):
	def __init__(self, username, password, person_obj, status = AccountStatus.ACTIVE):
		self.__username = username
		self.__password = password
		self.__person = person_obj
		self.__status = status

class Librarian(Account):
	def __init__(self, username, password, person_obj, status= AccountStatus.ACTIVE):
		super().__init__(username, password, person_obj, status)

	def add_book_item(self, book_item):
		pass

	def remove_book_item(self, book_item):
		pass

	def add_member(self, member):
		pass

	def remove_member(self, member):
		pass

class Member(Account):
	def __init__(self, username, password, person_obj, status= AccountStatus.ACTIVE):
		super().__init__(username, password, person_obj, status)
		self.__total_books_checkedout = 0

	def checkout_book_item(self, book_item):
		if self.get_total_books_checkedout() >= Constants.MAX_BOOKS_ISSUED_TO_A_USER:
			print("The user has already checked-out maximum number of books")
      	return False
      	book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())
      	if book_reservation != None and book_reservation.get_member_id() != self.get_id():
      		print("Book reserved for a different user")
      		return False
      	if book_reservation != None:
      		book_reservation.update_status(ReservationStatus.COMPLETED)
      	if not book_item.checkout(self.get_id()):
      		return False
	    self.increment_total_books_checkedout()
	    return True

	def renew_book_item(self, book_item):
		self.check_for_fine(book_item)
		book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())
		if book_reservation != None and book_reservation.get_member_id() != self.get_id():
			print("Reserved by different user")
			self.decrement_book_checkedout()
			book_item.update_status(ReservationStatus.RESERVED)
			book_reservation.send_book_avaiable_notification()
			return False
		elif book_reservation != None:
			book_reservation.update_status(ReservationStatus.COMPLETED)
		BookLending.lend_book(book_item, self.get_id())
		BookLending.update_due_date(datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))


	def return_book_item(self, book_item):
		self.check_for_fine(book_item)
		book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())
		if book_reservation != None:
			book_reservation.send_book_avaiable_notification()
		book_item.update_book_item_status(BookStatus.AVAILABLE)
		self.decrement_book_checkedout()

	def check_for_fine(self, book_item):
		book_lending = BookLending.fetch_lending_details(book_item)
		due_date = book_lending.get_due_date()
		today = datetime.date.today()
		if today > due_date:
			diff = today - due_date
			diff_days = diff.days
			Fine.collect_fine(self.get_member_id(), diff_days)

	def get_total_books_checkedout(self):
		return self.__total_books_checkedout

	def increment_book_checkedout(self):
		self.__total_books_checkedout += 1


class Book(ABC):
	def __init__(self, ISBN, title, subject, author, publisher, language):
		self.__ISBN = ISBN
		self.__title = title
		self.__subject = subject
		self.__author = author
		self.__publisher = publisher
		self.__language = language

class BookItem(Book):
  def __init__(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status, date_of_purchase, publication_date, placed_at):
    self.__barcode = barcode
    self.__is_reference_only = is_reference_only
    self.__borrowed = borrowed
    self.__due_date = due_date
    self.__price = price
    self.__format = book_format
    self.__status = status
    self.__date_of_purchase = date_of_purchase
    self.__publication_date = publication_date
    self.__placed_at = placed_at

  def checkout(self, member_id):
    if self.get_is_reference_only():
      print("self book is Reference only and can't be issued")
      return False
    if not BookLending.lend_book(self.get_bar_code(), member_id):
      return False
    self.update_book_item_status(BookStatus.LOANED)
    return True

  def get_barcode(self):
  	return self.__barcode

class Rack:
  def __init__(self, number, location_identifier):
    self.__number = number
    self.__location_identifier = location_identifier

class BookReservation:
  def __init__(self, creation_date, status, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__status = status
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def fetch_reservation_details(self, barcode):
    pass


class BookLending:
  def __init__(self, creation_date, due_date, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__due_date = due_date
    self.__return_date = None
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def lend_book(self, barcode, member_id):
    pass

  def fetch_lending_details(self, barcode):
    pass


class Fine:
  def __init__(self, creation_date, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def collect_fine(self, member_id, days):
    pass

class Search(ABC):

  def search_by_title(self, title):
    None

  def search_by_author(self, author):
    None

  def search_by_subject(self, subject):
    None

  def search_by_pub_date(self, publish_date):
    None


class Catalog(Search):
  def __init__(self):
    self.__book_titles = {}
    self.__book_authors = {}
    self.__book_subjects = {}
    self.__book_publication_dates = {}

  def search_by_title(self, query):
    # return all books containing the string query in their title.
    return self.__book_titles.get(query)

  def search_by_author(self, query):
    # return all books containing the string query in their author's name.
    return self.__book_authors.get(query)