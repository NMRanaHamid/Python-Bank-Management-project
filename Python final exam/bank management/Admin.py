from Bank import *
from User import *

class Admin(Bank) :
    def __init__(self,admin_id, password,bank):
        self.admin_id = 101
        self.password = 2441139
        self.allow = True
        self.bank = bank 
        if self.admin_id != admin_id or self.password != password:
            print("Sorry ! You are not an admin . You don't have permisson to enter into the admin panel")
            self.allow = False


    def create_account(self,name,email,nid,phone,address,account_type,password,bank):
        account = User(name,email,nid,phone,address,account_type,password,bank)
        self.bank.add_users(account)
        print("Create account done .")
        return account

    def delete_account(self, user_id):
        self.bank.delete_users(user_id)

    def show_user_accounts(self):
        self.bank.show_users()
    
    def check_balance(self):
        print(f"Total balance of the bank is : {self.bank.total_balance}")
    
    def check_total_loan(self):
        print(f"Total loan amount in the bank is {self.bank.total_loan}")

    def show_loan_status(self):
        print("current loan feature status :",end=' ')
        if self.bank.loan_feature_off :
            print("Off")
        else :
            print("On")
        
    def control_loan(self):
        self.bank.loan_feature_off ^= True 
        
        
