import logging
class DeleteRows:
    cnx = None
    logger = logging.getLogger()
    def __init__(self, cnx, logger):
        self.cnx = cnx
        self.logger = logger

    def deleteUserRow(self, uid):
        delete = "DELETE FROM users WHERE uid = %s"
        cursor = self.cnx.cursor()
        try:
            cursor.execute(delete, [uid])
            self.cnx.commit()
            self.logger.info("Deleted user from the users table")
            return True
        except Exception as e: 
            print("Delete input was invalid")
            self.logger.info("Failed to delete user from the users table")
            #print(e)
        return False
        

    def deleteBookRow(self, bid):
        delete = "DELETE FROM books WHERE bid = %s"
        cursor = self.cnx.cursor()
        try:
            cursor.execute(delete, [bid])
            self.cnx.commit()
            self.logger.info("Deleted book from the books table")
            return True
        except Exception as e: 
            print("Delete input was invalid")
            self.logger.info("Failed to delete book from the books table")
            #print(e)
        return False
        

    def deleteOrderRow(self, oid):
        delete = "DELETE FROM orders WHERE oid = %s"
        cursor = self.cnx.cursor()
        try:
            cursor.execute(delete, [oid])
            self.cnx.commit()
            self.logger.info("Deleted order from the orders table")
            return True
        except Exception as e: 
            print("Delete input was invalid")
            self.logger.info("Failed to delete order from the orders table")
            #print(e)
        return False
        