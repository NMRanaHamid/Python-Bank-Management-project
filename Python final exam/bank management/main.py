from Bank import *
from Admin import *
from User import *

bank = Bank('Dutch Bangla')
while True :
    print("\n******************************************")
    print("1.Admin login")
    print("2.User login")
    print("3.Create Account")
    print("4.Exit")
    choice = int(input("Enter your choice : "))
    print("\n*******************************************")
    if choice == 1:
        id = int(input("Enter your ID : "))
        password = int(input("Enter password : "))
        admin = Admin(id,password,bank)
        if admin.allow == False :
            continue
        else :
            while True :
                print("\n--------------------")
                print("1.Create account")
                print("2.Delete user account")
                print("3.See all user account")
                print("4.See total available balance")
                print("5.See total loan amount")
                print("6.Control the loan feature ")
                print("7.Exit")
                ad_choice = int(input("Enter your choice : "))
                if ad_choice == 1 :
                    name = input("Enter name : ")
                    email = input("Enter email : ")
                    nid = input("Enter nid : ")
                    phone = input("Enter phone : ")
                    address = input("Enter address : ")
                    account_type = input("Enter account type : ")
                    password = input("Enter password : ")
                    print("\n--------------------")
                    user = admin.create_account(name,email,nid,phone,address,account_type,password,bank)
                elif ad_choice == 2 :
                    print("\n--------------------")
                    user_id = int(input("Enter user ID : "))
                    admin.delete_account(user_id)
                elif ad_choice == 3 :
                    print("\n--------------------")
                    admin.show_user_accounts()
                elif ad_choice == 4 :
                    print("\n--------------------")
                    admin.check_balance()
                elif ad_choice == 5 :
                    print("\n--------------------")
                    admin.check_total_loan()
                elif ad_choice == 6 :
                    print("\n--------------------")
                    admin.show_loan_status()
                    print("You want to change ? : y/n")
                    ch = input("")
                    if(ch =='y' or ch=='Y'):
                        admin.control_loan()
                    else :
                        continue
                elif ad_choice == 7 :
                    break
                else :
                    print("Invalid Option.\n--------------------")
                print("-----------------------------")
    
    elif choice==2 :
        id = int(input("Enter your ID : "))
        password = input("Enter your password : ")
        user = Bank.find_user(bank,id,password)
        if user == None :
            print("There is no user at this information.")
        else :
            user.show_details()
            print("Do you want menu for your account ? : y/n")
            chn = input("")
            if chn=='y' or chn=='Y':
                while True :
                    print("\n+++++++++++++++++++++++++++++++++++++")
                    print("1.Deposite cash.")
                    print("2.Withdraw cash.")
                    print("3.Check available balance")
                    print("4.Check transition history")
                    print("5.Take a loan")
                    print("6.Transfer amount")
                    print("7.Show current status.")
                    print("8.Exit")
                    user_ch = int(input("Enter your choice : "))
                    if(user_ch==1):
                        print("\n+++++++++++++++++++++++++++++++++++++")
                        amount = int(input("Enter amount : "))
                        user.depostie(amount)
                    elif(user_ch==2):
                        print("\n+++++++++++++++++++++++++++++++++++++")
                        amount = int(input("Enter amount : "))
                        user.withdraw(amount)
                    elif(user_ch==3):
                        print("\n+++++++++++++++++++++++++++++++++++++")
                        user.current_balance()
                    elif(user_ch==4):
                        print("\n+++++++++++++++++++++++++++++++++++++")
                        user.transition_history()
                    elif(user_ch==5):
                        print("\n+++++++++++++++++++++++++++++++++++++")
                        amount = int(input("Enter amount : "))
                        user.take_loan(amount)
                    elif(user_ch==6):
                        print("\n+++++++++++++++++++++++++++++++++++++")
                        amount = int(input("Enter amount : "))
                        another_id= int(input("Enter another ID : "))
                        if(amount > user.balance):
                            print("Invalid amount.")
                            continue
                        user.transfer_money(amount,another_id)
                    elif user_ch == 7 :
                        user.show_details()
                    elif user_ch==8:
                        break
                    else :
                        print("Invalid option.\n+++++++++++++++++++++++++++++++++++++")
                    print("+++++++++++++++++++++++++++++++++++++")

            else :
                continue

    elif choice == 3:
        name = input("Enter name : ")
        email = input("Enter email : ")
        nid = input("Enter nid : ")
        phone = input("Enter phone : ")
        address = input("Enter address : ")
        account_type = input("Enter account type : ")
        password = input("Enter password : ")
        user = User(name,email,nid,phone,address,account_type,password,bank)
        
        print("congratulation ! you create your account successfully")
        bank.add_users(user)

    elif choice == 4:
        break
    else :
        print("Invalid option \n")