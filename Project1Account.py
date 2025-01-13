from Project1InsertRows import InsertRows
import logging
class Account:
    cnx = None
    logger = logging.getLogger()
    insertRows = InsertRows(cnx, logger)
    def __init__(self, cnx, logger):
        self.cnx = cnx
        self.logger = logger
        self.insertRows = InsertRows(cnx, logger)

    def login(self, user, password):
        
        cursor = self.cnx.cursor()

        loginQuery = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(loginQuery, (user, password))
        result = cursor.fetchall()
        loginSuccess = False
        if len(result) > 1:
            print("ERROR: No two users can have the save username and password")
            self.logger.info("Account login failed")
        elif len(result) == 1:
            result = result[0]
            loginSuccess = True
            self.logger.info("Account login succeeded")
        else:
            print("Username or password is incorrect")
            self.logger.info("Account login failed")
        
        return loginSuccess, result
    
        
