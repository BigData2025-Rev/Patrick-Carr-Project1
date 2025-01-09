from Project1InsertRows import InsertRows
class Account:
    cnx = None
    insertRows = InsertRows(cnx)
    def __init__(self, cnx):
        self.cnx = cnx
        self.insertRows = InsertRows(cnx)

    def login(self, user, password):
        
        cursor = self.cnx.cursor()

        loginQuery = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(loginQuery, (user, password))
        result = cursor.fetchall()
        loginSuccess = False
        if len(result) > 1:
            print("ERROR: No two users can have the save username and password")
        elif len(result) == 1:
            #print(result)
            result = result[0]
            #print(result)
            loginSuccess = True
        else:
            print("Username or password is incorrect")
        
        return loginSuccess, result
    
    # def createAccount(self, user, password):
        
    #     result = self.insertRows.insertUserRow(user,password,False,"0")
    #     if result:
    #         print("Account creation was successful")
        
    #     return result
        
