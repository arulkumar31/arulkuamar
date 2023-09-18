#2.1 implements a class called bankaccount that represents a bank account. The class should have private attributes for account number , account holder name , and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the bankaccount class and test the deposit and withdrawl functionality.

def_init_(self,account_number,account_holder_name, initial_balance=0.0):
self_account_number=account_number
self_account_holder_name=account_holder_name
self_account_balance-initital_balance


def deposit(self,amount):
if amount > 0:
self_account_balance+=amount
printf("deposited ${amount:.2f}into account{self_account_number}")
else:
printf("invalid deposit amount . please deposite a positive amount.")


def withdraw(self,amount):
if amount > 0:
if self_account_balance>=amount:
self_account_balance -=amount
printf("withdrew ${smount:.2f}from account{self_account_number}")
else:
print("insufficient balance.cannot withdraw.")
else:
print("invalid withdrawal amount. Please withdraw a positive amount.")

def display_balance(self):
printf("account{self_account_number}balance:${self_account_balance:.2f}")

#testing the bank account class 
If_name_=="__main__":
#create a bankaccount instance 
Account1=bankaccount("123456","john doe",1000.0)

#deposit money 
Account1.deposit(500.0)

#withdraw money
Account1.withdraw(200.0)

#display balance
Account1.display_balance()
