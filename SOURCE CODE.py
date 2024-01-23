class Atm:
    def __init__(self):
        self.__pin=0
        self.__balance=0
        self.login()
        
    # Function to select the login type
    def login(self):
        login_type=int(input("""
                                Please select the type of login:
                            
                             1. ENTER 1 FOR USER LOGIN
                             2. ENTER 2 FOR ADMIN LOGIN
                             3. ENTER 3 TO EXIT
                             
                             """))
        if login_type==1:
            print("You will be directed to USER page")
            self.__menu()
        elif login_type== 2:
            print("You will be directed to ADMIN login")
            self.administrative()    
        elif login_type==3:
            n=input("Do you want to exit (Y/N): ")
            if n.upper()=='Y':
                exit()
            elif n.upper()=='N':
                self.login()
            else:
                print("Invalid Input.")
                self.administrative()

# Function to get the pin of the user
    def get_pin(self):
        return self.__pin
    
# Function to get the balance of the user
    def check_balance(self):
        return self.__balance

# Function to change the pin of the user   
    def set_pin(self, new_pin):
        self.__pin= new_pin
        print("Pin changed")

# Function for ADMIN page
    def administrative(self):
        temp=int(input("Please enter ADMIN PIN: "))
        flag=True
        while flag:
                if temp== 123456:
                    admin=int(input("""
                             AS AN ADMIN YOU HAVE THE FOLLOWING FUNCTIONS:
                        1. ENTER 1 TO GET THE USER PIN
                        2. ENTER 2 TO CHANGE PIN
                        3. ENTER 3 TO CHECK BALANCE
                        4. ENTER 4 TO GO BACK
                            
                        """))
                    if admin== 1:
                        print("The PIN of the user is: ", self.__pin)
                    elif admin== 2:
                        pin=int(input("Please enter the new PIN: "))
                        self.set_pin(pin)
                    elif admin== 3:
                        balance=self.check_balance()
                        print("Balance of the user is: ", balance)
                    elif admin==4:
                        admin_choice=input("Do you want to exit (Y/N): ")
                        if admin_choice.upper()=='Y':
                            self.login()
                        elif admin_choice.upper()=='N':
                            self.administrative()
                        else:
                            print("Invalid input.")
                    else :
                        print("Invalid input.")
                        self.administrative()
# Function for USER page
    def __menu(self):
        while True:
            user_input=input("""
              Hello, how would you like to proceed?
                         1. Enter 1 to create pin
                         2. Enter 2 to deposit
                         3. Enter 3 to withdraw
                         4. Enter 4 to check balance
                         5. Enter 5 to go back
                          
                             """)
        
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.balance_check()
            elif user_input=="5":
                print("I hope your experience was good")
                self.rating()
                print("Thank you.")
                self.login()
                break
            else:
                print("Invalid input. Please enter correct input.")

# Function to create the PIN for the USER
    def create_pin(self):
        temp=int(input("Enter your pin: "))
        self.__pin=temp
        print("Pin set succesfully.")
        return temp

# Function for USER to deposit money
    def deposit(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            amount= int(input("Enter the amount: "))
            self.__balance= self.__balance+ amount
            print("Deposit successful.")
        else:
            print("Invalid pin. ")
    
# Function for the USER to withdraw the money
    def withdraw(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            amount= int(input("Enter the amount: "))
            if amount<self.__balance:
                self.__balance-=amount
                print("Operation successful.")
            else:
                print("Insufficient fund")
        else:
            print("Invalid pin. ")

# Function for the USER to check the balance
    def balance_check(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            print("Your account balance is: ",self.__balance)
        else:
            print("Invalid pin. ")

#  Function for the USER to rate the services
    def rating(self):
        service_rating=input(""" Enter the rating for the application on the basis of your experience:
                        1. Enter 5 for VERY GOOD experience
                        2. Enter 4 for GOOD experience
                        3. Enter 3 for AVERAGE experience     
                        4. Enter 2 for BELOW AVERAGE experience     
                        5. Enter 1 for POOR experience
                             """)
        if service_rating=='5':
            print("We are glad that you liked our service.")
        elif service_rating=='4':
            print("We are glad that you were satisfied by our services.")
            review=input("Please tell us the area of improvement: ")
        elif service_rating=='3':
            print("We are sorry that you found our service as average.")
            review=input("Please tell us the area of improvement: ")
        elif service_rating=='2':
            print("We are sorry that you did not like our service.")
            review=input("Please tell us the area of improvement: ")
        elif service_rating=='1':
            print("We are sorry that you did not like our service.")
            review=input("Please tell us the area of improvement: ")
        else:
            print("Invalid input")

    

class Bank:
    
    def __init__(self):
        self.name1=input("Bank Name: ")
        self.check_name()

    def check_name(self):
        print("You will now be transferred to the services of ", self.name1," bank")
        print("We hope you enjoy your experiences.")
        flag= True
        while flag:
            self.name1= Atm()

bank_service= Bank()
