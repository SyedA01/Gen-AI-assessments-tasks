class Customer:
    def __init__(self, customer_id, name, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def show_details(self):
        print(self.customer_id, self.name, self.phone, self.email)

class Account:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance

class Transaction:
    def __init__(self, transaction_id, account, amount):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount

    def process(self):
        print("Processing transaction...")


class Beneficiary:
    def __init__(self, name, account_number, bank_name):
        self.name = name
        self.account_number = account_number
        self.bank_name = bank_name

class Loan:
    def __init__(self, loan_id, customer, amount, interest_rate):
        self.loan_id = loan_id
        self.customer = customer
        self.amount = amount
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.amount * self.interest_rate

class Card:
    def __init__(self, card_number, customer):
        self.card_number = card_number
        self.customer = customer

    def block_card(self):
        print("Card blocked")

class ATM:
    def __init__(self, atm_id, location):
        self.atm_id = atm_id
        self.location = location

    def withdraw_cash(self, account, amount):
        account.withdraw(amount)

customer1 = Customer(
    "C001",
    "Abdul",
    "9876543210",
    "abdul@gmail.com"
)

account = Account(
    "ACC1001",
    customer1,
    10000
)

atm = ATM("ATM001", "Chennai")

customer1.show_details()

atm.withdraw_cash(account, 2000)

print(account.check_balance())