# Requirements
# User should be able to withdraw, transfer, CheckBalance, Deposit money
# ATM should be able to read card, dispense cash, take cash, take check, print reciepts, display current activity. 
# Each ATM should be linked to a Bank. 

# High level classes:

# 1. Card
# 2. ATM
# 3. Customer
# 4. Account
# 5. Reader
# 6. Printer
# 7. Cash dispenser
# 8. Deposit
# 9. Keypad
# 10. Screen
# 11. Bank
# 12. Transaction

from abc import ABC, abstractmethod


class Bank():
	def __init__(self, name, bank_code):
		self.__name = name
		self.__bank_code = bank_code

class ATM():
	def __init__(self, Id, location):
		self.__id = Id
		self.__location = location

		self.__cash_dispenser = CashDispenser()
		self.__keypad = Keypad()
		self.__screen = Screen()
		self.__printer = Printer()
		self.__cash_deposit = CashDeposit()
		self.__check_deposit = CheckDeposit()

	def authenticate_user(self):
		pass

	def make_transaction(self):
		pass

class CashDispenser:
  def __init__(self):
    self.__total_five_dollar_bills = 0
    self.__total_twenty_dollar_bills = 0

  def dispense_cash(self, amount):
    None

  def can_dispense_cash(self):
    None


class Keypad:
  def get_input(self):
    None


class Screen:
  def show_message(self, message):
    None

  def get_input(self):
    None


class Printer:
  def print_receipt(self, transaction):
    None

# from abc import ABC, abstractmethod


class DepositSlot(ABC):
  def __init__(self):
    self.__total_amount = 0.0

  def get_total_amount(self):
    return self.__total_amount


class CheckDepositSlot(DepositSlot):
  def get_check_amount(self):
    None


class CashDepositSlot(DepositSlot):
  def receive_dollar_bill(self):
    None


class Card():
	def __init__(self, name, number, expiry, pin):
		self.__name = name
		self.__number = number
		self.__expiry = expiry
		self.__pin = pin

class Account:
  def __init__(self, account_number):
    self.__account_number = account_number
    self.__total_balance = 0.0
    self.__available_balance = 0.0

  def get_available_balance(self):
    return self.__available_balance


class SavingAccount(Account):
  def __init__(self, withdraw_limit):
    self.__withdraw_limit = withdraw_limit


class CheckingAccount(Account):
  def __init__(self, debit_card_number):
    self.__debit_card_number = debit_card_number


class Customer:
  def __init__(self, name, address, email, phone, status):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__status = status
    self.__card = Card()
    self.__account = Account

  def make_transaction(self, transaction):
    None

  def get_billing_address(self):
    None

class Transaction(ABC):
  def __init__(self, id, creation_date, status):
    self.__transaction_id = id
    self.__creation_time = creation_date
    self.__status = status

  def make_transation(self):
    None


class BalanceInquiry(Transaction):
  def __init__(self, account_id):
    self.__account_id = account_id

  def get_account_id(self):
    return self.__account_id


class Deposit(Transaction):
  def __init__(self, amount):
    self.__amount = amount

  def get_amount(self):
    return self.__amount


class CheckDeposit(Deposit):
  def __init__(self, check_number, bank_code):
    self.__check_number = check_number
    self.__bank_code = bank_code

  def get_check_number(self):
    return self.__check_number


class CashDeposit(Deposit):
  def __init__(self, cash_deposit_limit):
    self.__cash_deposit_limit = cash_deposit_limit


class Withdraw(Transaction):
  def __init__(self, amount):
    self.__amount = amount

  def get_amount(self):
    return self.__amount


class Transfer(Transaction):
  def __init__(self, destination_account_number):
    self.__destination_account_number = destination_account_number

  def get_destination_account(self):
    return self.__destination_account_number