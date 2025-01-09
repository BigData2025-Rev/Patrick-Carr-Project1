import mysql.connector
from Project1Tables import Tables
from Project1Account import Account
from Project1InsertRows import InsertRows
from Project1ReadRows import ReadRows
from Project1UpdateRows import UpdateRows
from Project1Delete import DeleteRows
from Project1UI import UI

class Main:
    def connector(self):
        #InputPass = input("Input database password:")
        #cnx = mysql.connector.connect(user='root', password=InputPass,
        cnx = mysql.connector.connect(user='root', password='gunther2116',
                              host='127.0.0.1',
                              database='project1')
        
        ui = UI(cnx)
        tables = Tables(cnx)

        tables.createUsersTable()
        tables.createBooksTable()
        tables.createOrdersTable()

        ui.start()

        # account = Account(cnx)
        # insertRows = InsertRows(cnx)
        # readRows = ReadRows(cnx)
        # updateRows = UpdateRows(cnx)
        # deleteRows = DeleteRows(cnx)

        # insertRows.insertUserRow()
        # insertRows.insertBookRow()
        # insertRows.insertOrderRow()
        # insertRows.insertOrderRow()

        # readRows.readUsers()
        # readRows.readBooks()
        # readRows.readOrdersAdmin()
        # readRows.readOrdersUser(2)

        # updateRows.updateUsersRow()
        # updateRows.updateBooksRow()
        # updateRows.updateOrdersRow()

        #deleteRows.deleteUserRow()
        #deleteRows.deleteBookRow()
        #deleteRows.deleteOrderRow()



        # loginSuccess, result = account.login()
        # if loginSuccess:
        #     print("Login Successful")
        #     #print(result)
        # else:
        #     print("Login Failed")
        #     #print(result)
            

        # createSuccess, result = InsertRows.insertUserRow()
        # if createSuccess:
        #     print("Success!")
        #     print(result)
        # else:
        #     print("Failure :(")
        #     print(result)

        # cursor = cnx.cursor()

        # cursor.execute('INSERT INTO users (username, password) VALUES ("test2", "password2")')

        # cnx.commit()

        # cursor.close()
        # cnx.close()
        


if __name__ == "__main__":
    main = Main()
    main.connector()