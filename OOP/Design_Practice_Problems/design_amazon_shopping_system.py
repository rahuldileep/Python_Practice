# Requirements:

# 1. User should be able to search for items.
# 2. Should be able to add item to cart.
# 3. should be able to checkout the items and pay.
# 4. System should be able to add new catogory & new item.
# 5. Should be able to process the payment.
# 6. Should be able to send notification to respective departments and user.
# 7. Should be able to show status of an order.
# 8. User should be able to add review and rating to the product.

# Major Actors
# Admin
# Guest
# Member
# System

# Classes:

# Account
# Member
# Admin
# Guest
# Catelog
# ShoppingCart
# ProductCatogory
# Product
# ProdcutReview
# Order
# Payment
# Item
# OrderLog
# ShipmentLog
# Notification

class Account:
	def __init__(self, username, password, email, shipping_address, phone):
		self.__user_name = user_name
	    self.__password = password
	    self.__name = name
	    self.__email = email
	    self.__phone = phone
	    self.__shipping_address = shipping_address
	    self.__credit_cards = []
	    self.__bank_accounts = []

	 def add_new_product(self, product):
	 	pass

	 def add_review(self, review):
	 	pass

	 def reset_password(self):
	 	pass

class Customer(ABC):
	def __init__(self, cart, order):
		self.__cart = cart
		self.__order = order

	def add_item_to_cart(self, item):
		pass

	def remove_item_from_cart(self, item):
		pass

	def get_shopping_cart(self):
		return self.__cart

class Member(Customer):
	def __init__(self, account):
		self.__account = account

	def place_order(self):
		pass

class Guest(Customer):
	def register_account(self):
		pass

