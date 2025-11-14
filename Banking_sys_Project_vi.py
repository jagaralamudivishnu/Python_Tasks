#------------BANKING SYSTEM-------------------

#This is a basic banking system implementation in Python that allows users to create accounts, log in , deposts and withdrawl funds
# and check balances, and view mini statements. The System consists of two  classes: Account and Banking system.

class Account:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
#The account class is defined with three variables - username ,password & Balance.
#The __init__ method initializes these variables with the arguments passed while creating an object of this class.


#The class also contains four methods -- Deposits, withdraws, get_balance and get_mini_statement.

    def deposit(self, amount):
        self.balance += amount
        print(f"\nAmount deposited: {amount}\nTotal Balance: {self.balance}")

#The deposit method takes an argument amount and adds it to the balance variable.
#It then prints a message showing the deposited amount and the updated balance.

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nAmount withdrawn: {amount}\nTotal Balance: {self.balance}")
        else:
            print("Insufficient Balance")

#The withdraw method takes an argument amounnt and checks if the balance is greater than or equal to the amount to be withdrawn.
#If it is debuts the withdrawn amount from the balance.
#prints a message showing the withdrwan amount and updates balaces.

    def get_balance(self):
        return self.balance
    
#The get_balance method simply returns the current balance.

    def get_mini_statement(self):
        print("Mini statement:")
        print(f" username: {self.username}")
        print(f" Current balance: {self.balance}")

#The get_mini_statement method prints the username and current balance of the account.

class BankingSystem:
    def __init__(self):
        self.accounts = {}

#the BankingSystem class is defined. It has one instance Variable - accounts -
    
    def create_account(self, username, password):
        if username in self.accounts:
            print("username already exists")
        else:
            self.accounts[username] = Account(username, password)
            print("\nAccount created successfully")
            print("------WELCOME TO BANK-----------")
         
# The create_account method takes two arguments - username and password.
#It checks if the username is already exists in the accounts dictionary.
#If it does, it prints a message saying that the username is already exists.
#If it does not, it creates a new Account with the given username and password and adds it to the account dictionary.
#It then prints a message saying that the account was created successfully.

    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login Sucess...........")
                return account
            else:
                print("Invalid password")
        else:
            print("Invalid Username ")
        return None
# The login method takes two arguments - username and password. It checks if the given username exists in the acccounts dict.
#If it does, it retrieves the corresponding account object and checks if the given password matches the passwrd of that account.
#If it does, it prints a message saying that the login was successful and returns the Account object.
#If it does not, it prints a message saying taht the password is invalid. If the given username is not found in the account dicit, it prints a message saying that the username is invalid.

bank = BankingSystem()

while True:
    print("\n")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice(1-3): ")

#The main program loop is defined inside the if __name__ == '__main__': block.
#It creates a new BankingSystem obj  and presents a menu of options to user - create an account, login, or exit.

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(username, password)
#if the user chooses to create an account, the program prompts the user to enter a username and password.
#It then calls the create-account method of the BankingSystem obj with these arguments.

    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        Account = bank.login(username,password)
        if Account is not None:
            while True:
                print("\n----WELCOME TO BANK----")
                print("1.Deposit")
                print("2.Withdraw")
                print("3. Check BAlance")
                print("4. Mini Statement")
                print(" 5. Logout\n")
                choice = input("Enter your choice (1-5): ")
#If the user chooses to login, the program prompts the user to enter their username and password. It then calls the login method of the BankingSystem obj with these arguments.
#if the login is successful, it presents the user with a menu of options - deposit, withdraw, check balance, print mini-statement, or logout.

                if choice == '1':
                    amount = int(input("Enter amount to deposit: "))
                    Account.deposit(amount)
                elif choice == '2':
                    amount = int(input("Enter amount to withdraw: "))
                    Account.withdraw(amount)
# If the user chooses to deposit or withdraw, the program prompts the user to enter the amount to deposit or withdraw. It then calls the corresponding method of the Account object.

                elif choice == '3':
                    print(f"Current balance: {Account.get_balance()}")
# If the user chooses to check their balance, the program calls the get_balance method of the Account object and prints the current balance.

                elif choice == '4':
                    Account.get_mini_statement()
# If the user chooses to print a mini-statement, the program calls the get_mini_statement method of the Account object and prints the username and current balance.

                elif choice == '5':
                    print("\n--------THANK YOU VISIT AGAIN--------")
                    break
# If the user chooses to logout, break out of the inner WHILE loop and display a message saying "THANK YOU VISIT AGAIN".
                else:
                    print("Invalid choice")
    elif choice == '3':
        print("\n------THANK YOU------")
        break
# If the user selects option 3, a message is printed indicating that they have exited the program, and the break statement is used to exit the outer while loop that displays the main menu.

    else:
        print("Invalid choice")


# ----------- FINISHED ------- THANK YOU ---------