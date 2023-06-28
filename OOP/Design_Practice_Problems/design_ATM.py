"""
1.Requirements
 1.1 - User should be able to check balance, transfer and withdraw money
 1.2 - Each user should have a Savings and Checking account
 1.3 - ATM authenticates the user using the pin
 1.4 - ATM should have a screen, keypad, dispenser, printer, cardreader
 1.5 - User should have an option to end or start a new transaction in the end

2.Identify the main actors of the system
 2.1 - User
 2.2 - System
 2.3 - Cardissuer/BANK

3.Define actions/use cases for each actor
 3.1 - User
  - Insert Card
  - Change PIN
  - Transaction - Check Balance, Withdraw money, transfer
  - Cancel transaction
 3.2 - Cardissuer
  - Authenticate User
  - Check Transaction limit for account
  - Check sufficient funds in account
 3.3 - System/bank
  - Authenticate User
  - Check sufficient funds in ATM
  - Check ATM withdrawal limit
  - Dispense money
  - Print receipt
  - Return Card

4.Identify extend and include relationships between use cases
 4.1 - "Transaction" use case has an extend relationship with "print receipt" use case because we have an option to get the receipt
 4.2 - "Insert Card" use case has an include relationship with "Authenticate user" use cases in both Cardissuer and System
 4.3 - "Transfer" use case has an include relationship with "Check sufficient" and "Check Transaction limit" in account
 4.4 - "Withdraw money" use case has include relationships with "Check sufficient funds in ATM", "Check ATM withdrawal limit",
       "Check Transaction limit for account", "Check sufficient funds in account". 
     - Also, "Withdraw money" use case has include relationship"Dispense money".
 4.5 - "Transaction" use case and the "Cancel Transaction" use case have an include relationship with the "Return card" use case

5.Identify components/Classes of the system
 - User
 - ATM
 - ATMCard
 - ATMRoom
 - Bank
 - BankAccount - SavingAccount, CheckingAccount
 - Screen
 - Keypad
 - Printer
 - CardReader
 - CashDispenser
 - ATMState -  CheckBalanceState, CashWithdrawalState, TransferMoneyState, HasCardState, IdleState, SelectOperationState 
 - Enums

6.Identify Association, Composition, Inheritance relationships
 6.1 - Association
  - ATMRoom has one-way relationship with ATM and User
  - User class has one-way relationship with BankAccount and ATMCard classes
  - ATMCard has one-way relationship with BankAccount
  - ATM class has one-way relationship with Bank and ATMState

 6.2 - Composition
  - ATM class has Composition relationship with Screen, Keypad, Printer, CardReader, CashDispenser

 6.3 - Inheritance
  - Both, SavingAccount and CurrentAccount, extend the BankAccount class.
  - The CheckBalanceState, CashWithdrawalState, TransferMoneyState, HasCardState, IdleState, and SelectOperationState classes 
      extend the abstract class, ATMState.

7.Class Diagram

8.Design Pattern
 8.1 - The Singleton design pattern
     This pattern ensures the existence of a single instance of the ATM at a given moment 
     that can be accessed by multiple users, due to the shared nature of the ATM components
 8.2 - The State design pattern
     This pattern enables the ATM to alter its behavior based on the internal changes in the machine. 
     This way, an ATM can transition from one state to another and as soon as all the operations have 
     been performed, it can switch back to the initial idle state

9.Enums
 9.1 - ATMState
  - Idle
  - Card inserted by the user
  - Option selected
  - Cash withdrawal
  - Transfer money
  - Display the account balance

 9.2 - TransactionType
  - Balance inquiry
  - Cash withdrawal
  - transfer

10.Code
"""

from enum import Enum
from abc import ABC, abstractmethod

class ATMStatus(Enum):
  Idle = 1
  HasCard = 2
  SelestionOption = 3
  Withdraw = 4
  TransferMoney = 5
  BalanceInquiry = 6

class TransactionType(Enum):
  Balance_inquiry = 1
  Withdraw = 2
  Transfer = 3

class User:
  def __init__(self, card, account):
    self.__card = card
    self.__account = account

class ATMCard:
  def __init__(self, cardNumber, customerName):
    self.__cardNumber = cardNumber
    self.__customerName = customerName

class BankAccount:

  def __init__(self, account_number, available_balance):
    self.__account_number = account_number
    self.__available_balance = available_balance

  def get_available_balance(self):
    return self.__available_balance

class SavingsAccount(BankAccount):

  def __init__(self, account_number, available_balance):
    super().__init__(account_number, available_balance)

  def get_withdrawal_limit(self):
    pass


class CheckingAccount(BankAccount):
  def __init__(self, account_number, available_balance):
    super().__init__(account_number, available_balance)

  def get_withdrawal_limit(self):
    pass

class Bank:
  def __init__(self, name, bankcode):
    self.__name = name
    self.__bankcode = bankcode

class CardReader:
  def readCard():
    pass

class CashDispenser:
  def dispenseCash():
    pass

class Keypad:
  def getInput():
    pass

class Screen:
  def showMessage():
    pass

class Printer:
  def printReceipt():
    pass

class ATM:
  __currentATMState = None

  def __init__(self, currentATMState, atmBalance, noOfHundredDollarBills, noOfFiftyDollarBills, noOfTenDollarBills):
    self.atmBalance = atmBalance
    self.noOfHundredDollarBills = noOfHundredDollarBills
    self.noOfFiftyDollarBills = noOfFiftyDollarBills
    self.noOfTenDollarBills = noOfTenDollarBills
    self.changestate(currentATMState)

  def changestate(self, state):
    self.__currentATMState = state
    self.__currentATMState.atm = self

  def displayCurrentState(self):
    print(self.__currentATMState)


class ATMRoom:
  def __init__(self, atm, user):
    self.__atm = atm
    self.user = user

class ATMState:

  @property
  def atm(self):
    return self.__atm_context

  @atm.setter
  def atm(self, atm):
    self.__atm_context = atm

  @abstractmethod
  def insertCard(self, atm, card):
    pass

  @abstractmethod
  def authenticatePin(self, atm, card, pin):
    pass

  @abstractmethod
  def selectOperation(self, atm, card, transactionType):
    pass

  @abstractmethod
  def cashWithdrawal(self, atm, card, withdrawAmount):
    pass

  @abstractmethod
  def displayBalance(self, atm, card):
    pass

  @abstractmethod
  def transferMoney(self, atm, card, accountNumber, transferAmount):
    pass

  @abstractmethod
  def returnCard(self):
    pass

  @abstractmethod
  def exit(self, atm):
    pass

class IdleState(ATMState):
  def insertCard(self, atm, card):
    pass

  def handle(self):
    pass

  def returnCard(self):
    pass

  def exit(self, atm):
    pass

class HasCardState(ATMState):
  def authenticatePin(self, atm, card, pin):
    pass

  def returnCard(self):
    pass

  def exit(self, atm):
    pass
    
class SelectOperationState(ATMState):
  def selectOperation(self, atm, card, transactionType):
    pass

  def returnCard(self):
    pass

  def exit(self, atm):
    pass

class CheckBalanceState(ATMState):
  def displayBalance(self, atm, card):
    pass

  def returnCard(self):
    pass

  def exit(self, atm):
    pass

class CashWithdrawalState(ATMState):
  def cashWithdrawal(self, atm, card, withdrawAmount):
    pass

  def returnCard(self):
    pass

  def exit(self, atm):
    pass

class TransferMoneyState(ATMState):
  def transferMoney(self, atm, card, accountNumber, transferAmount):
    pass

  def returnCard(self):
    pass

  def exit(self, atm):
    pass

