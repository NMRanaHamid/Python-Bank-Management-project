from Bank import *
from Admin import *
class User  :
    acc_no = 10001
    def __init__(self,name,email,nid,phone,address,account_type,password,bank):
        self.name = name
        self.email = email
        self.nid = nid 
        self.phone = phone 
        self.address = address 
        self.account_type = account_type
        self.password = password
        self.balance = 0
        self.user_id = User.acc_no
        User.acc_no += 1 
        self.loan = 0
        self.transition = []
        self.bank = bank 

    def depostie(self,amount):
        if amount>0 :
            self.balance += amount
            s = f"Deposite cash amount of : {amount}"
            self.transition.append(s)
            print(f"Successfully deposite tk {amount}")
        else :
            print("Invalid amount.")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Sorry ! Withdrawal amount exceeded")
        else :
            self.balance -= amount 
            print(f"Successfully withdraw {amount} tk.")
            s = f"Withdraw cash amount of : {amount}"
            self.transition.append(s)
    def current_balance(self):
        print(f"Your current balance is : {self.balance}")
        print(f"Your due loan is tk {self.loan}")

    def take_loan(self,amount):
        grant = self.bank.grant_loan(amount)
        if grant == True :
            self.loan += amount
            s = f"Take loan amount of : {amount}"
            self.transition.append(s)

    def transfer_money(self,amount,another_account_id):
        grant = self.bank.grant_transfer_money(amount,another_account_id)
        if grant == True :
            self.balance -= amount
            s = f"Transfer to account {another_account_id} amount of : {amount}"
            self.transition.append(s)

    def transition_history(self):
        for s in self.transition :
            print(s)

    def show_details(self):
        print("My status :")
        print(f"Name : {self.name}")
        print(f"User ID : {self.user_id}")
        print(f"NID : {self.nid}")
        print(f"Email : {self.email}")
        print(f"Phone : {self.phone}")
        print(f"Addrees : {self.address}")
        print(f"Account type : {self.account_type}")
        print(f"Current Balance : {self.balance}")
        print(f"Current loan : {self.loan}")
