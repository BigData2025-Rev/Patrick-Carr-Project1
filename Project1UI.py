from Project1Account import Account
from Project1InsertRows import InsertRows
from Project1ReadRows import ReadRows
from Project1UpdateRows import UpdateRows
from Project1Delete import DeleteRows
from Project1Delete import DeleteRows
from datetime import datetime


class UI:
    cnx = None
    account = Account(cnx)
    insertRows = InsertRows(cnx)
    readRows = ReadRows(cnx) 
    updateRows = UpdateRows(cnx)
    deleteRows = DeleteRows(cnx)

    def __init__(self, cnx):
        self.cnx = cnx
        #Make new instances with the updated cnx
        self.account = Account(cnx)
        self.insertRows = InsertRows(cnx)
        self.readRows = ReadRows(cnx) 
        self.updateRows = UpdateRows(cnx)
        self.deleteRows = DeleteRows(cnx)
        
    def start(self):
        while True: #The loop is exited by choosing "3"
            loop = True
            option= input("""Do you want to log in, create an account, or quit?
                        1: Log in
                        2: Create an account
                        3: Quit
                    """)
            if option == "1":
                user = input("Input username:")
                password = input("Input password:")
                loginSuccess, result = self.account.login(user, password)
                if loginSuccess:
                    if result[3]:#Result[3] is the admin field of the user row from the login
                        self.adminCommands(result)
                    else: 
                        self.userCommands(result)

            elif option == "2":
                user = input("Input new account username:")
                password = input("Input new account password:")
                loop = True
                while loop:
                    admin = input(#You can create admin accounts for demonstration's sake
                        """Which role for this account?
                            1: Admin
                            2: User
                        """)
                    if admin == "1" or admin == "2":
                        loop = False
                    else:
                        print("Invalid input")
                adminBool = False
                if admin == "1":
                    adminBool = True

                result = self.insertRows.insertUserRow(user,password,adminBool,"0")
                if result:
                    print("Account creation was successful")
            elif option == "3":
                break #Quit was selected, so break the loop and return to the main class
            else:
                print("Invalid Input")

    def userCommands(self, user):
        while True: #The loop is exited by choosing "4"
            option= input("""What do you want to do?
                            1: View books
                            2: Make a purchase
                            3: View order history
                            4: Add funds
                            5: View funds
                            6: Quit
                        """)
            if option == "1":
                self.readRows.readBooks()
            elif option == "2":
                self.purchaseUI(user[0])#user[0] is uid
            elif option == "3":
                self.readRows.readOrdersUser(user[0])
            elif option == "4":
                funds = input("Input amount of added funds:")
                result = self.updateRows.updateUsersRow("","","",user[0],funds,True)
                if result:
                    print("Funds added successfully!")
            elif option == "5":
                print("Funds: " + str(self.readRows.readUserFunds(user[0])))
            elif option == "6":
                break #Quit was selected, so break the loop and return to the main class
            else:
                print("Invalid input")
    
    def purchaseUI(self, uid):
        print("The books are shown below:")
        self.readRows.readBooks()
        print("Funds: " + str(self.readRows.readUserFunds(uid)))
        bid = input("Input the Book ID for the book you wish to purchase:")
        purchases = input("How many do you wish to purchase?")
        result = self.updateRows.executePurchase(purchases, uid, bid) #Purchase needs a special function for ACID compliance
        if result:
            print("Purchase Successful")

    def adminCommands(self, admin):
        while True: #The loop is exited by choosing "4"
            option = input("""What do you want to do?
                            1: View books
                            2: Make a purchase
                            3: View order history
                            4: Add funds
                            5: View funds
                            6: Quit
                            7: Create a table row
                            8: Read a table
                            9: Update a table row
                            10: Delete a table row
                        """)
            if option == "1":
                self.readRows.readBooks()
            elif option == "2":
                self.purchaseUI(admin[0])#user[0] is uid
            elif option == "3":
                self.readRows.readOrdersUser(admin[0])
            elif option == "4":
                funds = input("Input amount of added funds:")
                result = self.updateRows.updateUsersRow("","","",admin[0],funds,True)
                if result:
                    print("Funds added successfully!")
            elif option == "5":
                print("Funds: " + str(self.readRows.readUserFunds(admin[0])))
            elif option == "6":
                break #Quit was selected, so break the loop and return to the main class
            elif option == "7":
                self.adminCreateUI()
            elif option == "8":
                self.adminReadUI()
            elif option == "9":
                self.adminUpdateUI()
            elif option == "10":
                self.adminDeleteUI()
            else:
                print("Invalid input")

    def adminCreateUI(self):
        while True:
            option = input("""Which table to create a row in?
                                1: Users
                                2: Books
                                3: Orders
                                4: Quit
                            """)
            if option == "1":
                self.insertUsersUI()
            elif option == "2":
                self.insertBooksUI()
            elif option == "3":
                self.insertOrdersUI()
            elif option == "4":
                break #Quit was selected, so break the loop and go back to the main admin command selection

    def adminReadUI(self):
        while True:
            option = input("""Which table to read?
                                1: Users
                                2: Books
                                3: Orders
                                4: Quit
                            """)
            if option == "1":
                self.readRows.readUsers()
            elif option == "2":
                self.readRows.readBooks()
            elif option == "3":
                self.readRows.readOrdersAdmin()
            elif option == "4":
                break #Quit was selected, so break the loop and go back to the main admin command selection

    def adminUpdateUI(self):
        while True:
            option = input("""Which table to update a row in?
                                1: Users
                                2: Books
                                3: Orders
                                4: Quit
                            """)
            if option == "1":
                self.updateUsersUI()
            elif option == "2":
                self.updateBooksUI()
            elif option == "3":
                self.updateOrdersUI()
            elif option == "4":
                break #Quit was selected, so break the loop and go back to the main admin command selection

    def adminDeleteUI(self):
        while True:
            option = input("""Which table to delete a row in?
                                1: Users
                                2: Books
                                3: Orders
                                4: Quit
                            """)
            if option == "1":
                self.deleteUsersUI()
            elif option == "2":
                self.deleteBooksUI()
            elif option == "3":
                self.deleteOrdersUI()
            elif option == "4":
                break #Quit was selected, so break the loop and go back to the main admin command selection

    def updateUsersUI(self):
        print("Updating row in the users table. Enter no input to keep a cell the same")
        uid = input("Input user ID to update:")
        username = input("Input updated username:")
        password = input("Input updated password:")
        admin = input(
            """Which role for the user?
                1: Admin
                2: User
            """)
        while admin != str(1) and admin != str(2) and admin != "":
            print("Input 1 or 2")
            admin = input(
            """Is the user an admin?
                1: True
                2: False
            """)
        fundsOption = input(
            """Which funds action?
                1: Add
                2: Set
            """)
        funds = input("Input amount:")
        add = False
        if fundsOption == "1":
            add = True
        adminBool = False
        if admin == "1":
            adminBool = True
        result = self.updateRows.updateUsersRow(username, password, adminBool, uid, funds, add)
        if result:
            print("Update successful!")

    def updateBooksUI(self):
        print("Updating row in the users table. Enter no input to keep a cell the same")
        #Do not loop
        bid = input("Input book ID to update:")
        bookname = input("Input updated book name:")
        author = input("Input updated author name:")
        
        release = input("Input updated release year:")

        price = input("Input price:")

        amount = input("Input book amount:")
        result = self.updateRows.updateBooksRow(bookname, author, release, price, amount,bid, False)
        if result:
            print("Update successful!")

    def updateOrdersUI(self):
        print("Inserting row into the orders table. Enter no input to keep a cell the same")

        oid = input("Input order id:")

        uid = input("Input new user id:")

        bid = input("Input new book id:")
        
        purchases = input("Input a purchase number:")
        spent = input("Input spent amount:")

        loop = True
        while loop:
            option = input(
                """Which kind of date & time input?
                    1: Current date & time
                    2: Custom date & time
                """)
            if option == "1" or option == "2" or option == "": #"" for keep the same
                loop = False
                break
            else:
                print("Input 1 or 2")
        result = self.updateRows.updateOrdersRow(uid, bid, option, purchases, oid, spent)
        if result:
            print("Update successful!")

    def insertUsersUI(self):
        print("Inserting row into the users table")
        username = input("Input new username:")
        password = input("Input new password:")

        loop = True
        while loop:
            admin = input(
                """Which role for the user?
                    1: Admin
                    2: User
                """)
            if admin == "1" or admin == "2":
                loop = False
            else:
                print("Invalid input")
        adminBool = False
        if admin == "1":
            adminBool = True
        funds = input("Input funds:")
        result = self.insertRows.insertUserRow(username, password, adminBool, funds)
        if result:
            print("Row creation successful!")
    
    def insertBooksUI(self):
        print("Inserting row into the books table")
        bookname = input("Input book name:")
        author = input("Input author name:")
        release = input("Input release year:")
        price = input("Input price:")
        amount = input("Input book amount:")
        result = self.insertRows.insertBookRow(bookname, author, release, price, amount)
        if result:
            print("Row creation successful!")
    
    def insertOrdersUI(self):
        print("Inserting row into the orders table")
        
        uid = input("Input user id:")

        bid = input("Input book id:")
        
        purchases = input("Input a purchase number:")
        spent = input("Input spent number:")

        loop = True
        while loop:
            option = input(
            """Which kind of date & time input?
                1: Current date & time
                2: Custom date & time
            """)
            if option == "1" or option == "2":
                loop = False
            else:
                print("Input 1 or 2")
        result = self.insertRows.insertOrderRow(uid, bid, option, purchases, spent)
        if result:
            print("Row creation successful!")

    def deleteUsersUI(self):
        uid = input("Input ID of the user to delete:")
        result = self.deleteRows.deleteUserRow(uid)
        if result:
            print("Deletion successful!")

    def deleteBooksUI(self):
        bid = input("Input ID of the book to delete:")
        result = self.deleteRows.deleteBookRow(bid)
        if result:
            print("Deletion successful!")

    def deleteOrdersUI(self):
        oid = input("Input ID of the order to delete:")
        result = self.deleteRows.deleteOrderRow(oid)
        if result:
            print("Deletion successful!")
        