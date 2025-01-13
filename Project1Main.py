import mysql.connector
from Project1Tables import Tables
from Project1Account import Account
from Project1InsertRows import InsertRows
from Project1ReadRows import ReadRows
from Project1UpdateRows import UpdateRows
from Project1Delete import DeleteRows
from Project1UI import UI
import logging

class Main:
    def connector(self):

        cnx = mysql.connector.connect(user='root', password='gunther2116',
                              host='127.0.0.1',
                              database='project1')
        
        logging.basicConfig(filename='bookstore_log.log', level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.info("Database connection established")
                
        ui = UI(cnx, logger)
        tables = Tables(cnx, logger)

        tables.createUsersTable()
        tables.createBooksTable()
        tables.createOrdersTable()

        ui.start()
        


if __name__ == "__main__":
    main = Main()
    main.connector()