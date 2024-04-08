class Bank :
    _users = []
    def __init__(self,name):
        self.name = name 
        self.total_balance = 10000000
        self.total_loan = 0
        self.loan_feature_off = False
    
    def add_users(self,user):
        self._users.append(user)
        self.total_balance += user.balance

    def show_users(self):
        if not self._users:  
            print("No users found.")
        for user in self._users :
            print(f"Name : {user.name}\nUser ID : {user.user_id}")

    def delete_users(self,user_id):
        if not self._users:  
            print("No users found.")
        for user in self._users :
            if user.user_id == user_id :
                self._users.remove(user)
                print("Delete accont done .")

    def grant_loan(self,amount):
        if amount> self.total_balance//5 :
            print("We can't provide you the loan")
            return False
        else :
            self.total_balance -= amount
            self.total_loan += amount
            print("Congratulation ! You got the loan.")
            return True 
    
    def grant_transfer_money(self, amount,another_account_id):
        found = False
        for user in self._users :
            if user.user_id == another_account_id :
                user.balance += amount
                print("Seccessfully Transferred money !")
                found = True 
        if found == False :
            print("There is no account on this user ID.")
        return found 

    def find_user(self,user_id,password):
        for user in self._users:
            if user.user_id == user_id and user.password ==  password :
                return user
        return None