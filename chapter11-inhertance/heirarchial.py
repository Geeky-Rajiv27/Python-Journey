'''
------------------------------------------Practice no. 1------------------------------------------------------
1. Banking System

Scenario:

Base class: BankAccount → attributes: account_no, balance, methods: deposit(), withdraw().

Derived classes:

SavingsAccount → adds interest_rate.
CurrentAccount → adds overdraft_limit.
FixedDeposit → adds maturity_date.

Task:

Implement the classes.

Create objects for each account type and perform deposit/withdraw operations.

Display all account details.
'''


'''--------------------------------------important NOTE---------------------------------------
    #NOTE:
    2. datetime.strptime("2028-01-27", "%Y-%m-%d")
datetime.strptime() means string-parse-time.

It converts a string into a datetime object, using the format you tell it:

%Y → 4-digit year
%m → 2-digit month
%d → 2-digit day

So "2028-01-27" becomes a real datetime.datetime(2028, 1, 27, 0, 0) object.

3. .date()
The .date() method extracts just the date part (without hours/minutes/seconds).
So now you get datetime.date(2028, 1, 27).
    
  -----------------------------------------------------------------------------------------------  '''

from datetime import date,datetime


class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
    
    def deposit(self):
        depobalance =  float(input(("Enter the balance you want to deposit to your current balance : ")))
        self.depobalance = depobalance
        self.balance = self.balance + self.depobalance

    def withdraw(self):
        drawbalance = float(input(("enter the withdraw amount you want to withdraw :")))
        self.drawbalance = drawbalance
        self.balance = self.balance - self.drawbalance

    def account_details(self):
        print(f"Your account no is : Rs.{self.account_no} ")
        print(f"Your current balance in your account is : Rs.{self.balance} \n")
    
class SavingsAccount(BankAccount):
    def __init__(self, Saving_balance, interest_rate = 6.5):
      
      self.Saving_balance = Saving_balance
      self.interest_rate = interest_rate
        
    def add_interest(self):
        self.interest_amount = self.Saving_balance * self.interest_rate
        self.Saving_balance = self.Saving_balance + self.interest_amount

    def  SavingAccount_details(self):
        print(f"You have got your interst amount in this account is : Rs. {self.interest_amount}")
        print(f"Your Saving account balance is : Rs. {self.Saving_balance}\n")


class CurrentAccount(BankAccount):
    overdraftlimit = 2000
    lent = 0
    def __init__(self,currAccBalance):
        self.currAccBalance = currAccBalance

    def Currentwithdraw(self):
        withdraw_amount = float(input("enter the amount you want to withdraw from your current account : "))
        self.withdraw_amount = withdraw_amount
        
        if(self.withdraw_amount <= self.currAccBalance):
            self.currAccBalance = self.currAccBalance - self.withdraw_amount
            print(f"Balance in your account is deducted by Rs. {self.withdraw_amount}\n")
            
        elif((self.withdraw_amount > self.currAccBalance) and (self.withdraw_amount < (self.currAccBalance + self.overdraftlimit))):
            self.lent = self.currAccBalance - self.withdraw_amount     # this is the amount bank lent to user (-ve ma hunxa)
            print(f"Bank has lent you {self.lent}")
            self.currAccBalance = 0

        else:
            print("Withdraw failed !, since your withdrawal amount is more even after adding over draft limit amount\n")

    def CurrentAccount_details(self):
        print(f"Your current account balance is now : Rs. {self.currAccBalance}")
        print(f"Now, you have dept of Rs.{self.lent} to bank \n")

class FixedAccount(BankAccount):
    amount_to_be_added = 200000 # this is the amount that is going to be added to the balance after maturity date
    maturity_date = datetime.strptime("2025-09-23", "%Y-%m-%d").date()
    fixed_date = date.today()
    def __init__(self, Fixed_balance):
        self.Fixed_balance = Fixed_balance
  
    
    def fixwithdraw(self):
        withdrawAmount_of_fix = float(input("enter the amount you want to withdraw form your Fixed account : "))
        self.withdrawAmount_of_fix = withdrawAmount_of_fix
        
        if((self.fixed_date) == self.maturity_date):
            self.Fixed_balance = (self.Fixed_balance + self.amount_to_be_added) - self.withdrawAmount_of_fix

        else:
            print("Against our Contract❌")
            print("Withdrawal from your fixed account is failed ! since you haven't reached the maturity date\n")
        
        print(f"Your balance in fixed account is Rs. {self.Fixed_balance}")
        

#all about bank account (checking all features)
b_acc = BankAccount(2006, 1000)
b_acc.account_details()
b_acc.deposit()
b_acc.account_details()

#withdrawing from bankaccount
b_acc.withdraw()
b_acc.account_details() #checking account details 


# #Checking saving account features
# s_acc = SavingsAccount(4000)
# s_acc.add_interest()
# s_acc.SavingAccount_details()


# #Checking feature of Current bank account
#     #NOTE CASE :1) withdrawing from the current balance (taking 1000 Rs loan from the bank)
# c_acc = CurrentAccount(300000)
# c_acc.Currentwithdraw()
#   #case A : i want to withdraw Rs.500 that is possible then :
#   #Case B : i want to withdraw total Rs.2000 using Rs 1000 of overdraft
#   #case C : i want to withdraw Rs 5000 which is not possible
# c_acc.CurrentAccount_details()


# #Checking feature of Fixed account
f_acc = FixedAccount(300000)
f_acc.fixwithdraw()





