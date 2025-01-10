import pandas as pd

class ReadRows:
    cnx = None
    def __init__(self, cnx):
        self.cnx = cnx
    
    #Admin Only
    def readUsers(self):
        print("Reading users")
        cursor = self.cnx.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            df = pd.DataFrame(result)
            df.columns = ['User ID', 'Username', 'Password', 'Admin (1 is true, 0 is false)', 'Funds']
            print(df)
        else:
            print("No users exsist.")
    
    #User and Admin
    def readBooks(self):
        print("Reading books")
        cursor = self.cnx.cursor()
        query = "SELECT * FROM books"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            df = pd.DataFrame(result)
            df.columns = ['Book ID', 'Title', 'Author', 'Release Year', 'Price', 'Amount']
            print(df)
        else:
            print("No books are available.")
        #for i in result:
        #    print("Book ID:" + str(i[0]) + "  Title:" + i[1] + "  Author:" + i[2] + "  Release Year:" + str(i[3]) + "  Price:$" + str(i[4]) + "  Amount:" + str(i[5]))
        #print(result[0][1])
        #print(result)
    
    def readOrdersAdmin(self):
        print("Reading orders")
        cursor = self.cnx.cursor()
        query = "SELECT * FROM orders"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            df = pd.DataFrame(result)
            df.columns = ['Order ID', 'User ID', 'Book ID', 'Date & Time', 'Purchases', 'Spent']
            print(df)
        else:
            print("No orders have been made")
    
    def readOrdersUser(self, uid):
        print("Reading orders")
        cursor = self.cnx.cursor()
        query = "SELECT * FROM orders WHERE orders.uid = %s"
        cursor.execute(query,[uid])
        result = cursor.fetchall()
        if len(result) > 0:
            df = pd.DataFrame(result)
            df.columns = ['Order ID', 'User ID', 'Book ID', 'Date & Time', 'Purchases', 'Spent']
            print(df)
        else:
            print("No orders have been made")

    def readUserFunds(self,uid):
        cursor = self.cnx.cursor()
        query = "SELECT * FROM users WHERE uid = %s"
        try:
            cursor.execute(query,[uid])
            result = cursor.fetchone()
            return result[4]
        except:
            return 0

    def readBookAmount(self,bid):
        cursor = self.cnx.cursor()
        query = "SELECT * FROM books WHERE bid = %s"
        try:
            cursor.execute(query,[bid])
            result = cursor.fetchone()
            return result[5]
        except:
            return 0
    
    def readBookPrice(self,bid):
        cursor = self.cnx.cursor()
        query = "SELECT * FROM books WHERE bid = %s"
        try:
            cursor.execute(query,[bid])
            result = cursor.fetchone()
            return result[4]
        except:
            return 0
        
