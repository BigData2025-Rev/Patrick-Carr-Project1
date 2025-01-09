class DeleteRows:
    cnx = None
    def __init__(self, cnx):
        self.cnx = cnx

    def deleteUserRow(self, uid):
        delete = "DELETE FROM users WHERE uid = %s"
        cursor = self.cnx.cursor()
        try:
            cursor.execute(delete, [uid])
            self.cnx.commit()
            return True
        except Exception as e: 
            print("Delete input was invalid")
            print(e)
        return False
        

    def deleteBookRow(self, bid):
        delete = "DELETE FROM books WHERE bid = %s"
        cursor = self.cnx.cursor()
        try:
            cursor.execute(delete, [bid])
            self.cnx.commit()
            return True
            #print("Delete Successful")
        except Exception as e: 
            print("Delete input was invalid")
            print(e)
        return False
        

    def deleteOrderRow(self, oid):
        delete = "DELETE FROM orders WHERE oid = %s"
        cursor = self.cnx.cursor()
        try:
            cursor.execute(delete, [oid])
            #print("Delete Successful")
            self.cnx.commit()
            return True
        except Exception as e: 
            print("Delete input was invalid")
            print(e)
        return False
        