#Admin Only
from Project1InsertRows import InsertRows
from datetime import datetime
from Project1ReadRows import ReadRows
from Project1InsertRows import InsertRows
import logging

class UpdateRows:
    cnx = None
    logger = logging.getLogger()
    readRows = ReadRows(cnx, logger)
    insertRows = InsertRows(cnx, logger)
    def __init__(self, cnx, logger):
        self.cnx = cnx
        #Make new instances with the updated cnx
        self.readRows = ReadRows(cnx, logger) 
        insertRows = InsertRows(cnx, logger)
        self.logger = logger

    def executePurchase(self, purchases, uid, bid):
        cursor = self.cnx.cursor()
        try: #If subtract is true, such as when purchasing, subtract the new value from the old one
            oldAmount = self.readRows.readBookAmount(bid)
            amount = int(oldAmount) - int(purchases)
            price = float(purchases) * float(self.readRows.readBookPrice(bid))
            funds = float(self.readRows.readUserFunds(uid)) - price
            fundsQuery = "UPDATE users SET funds = %s WHERE uid = %s"
            cursor.execute(fundsQuery, [funds,uid])
            booksQuery = "UPDATE books SET amount = %s WHERE bid = %s"
            cursor.execute(booksQuery, [amount,bid])
            insertRow = "INSERT INTO orders (uid, bid, orderTime, purchases, spent) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insertRow, (uid, bid, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), purchases, price))
            self.cnx.commit()
            self.logger.info("Purchase executed")
            return True
        except Exception as e: 
            print("Invalid purchase input")
            self.logger.info("Failed to execute purchase")
            #print(e)
        return False


    def updateUsersRow(self, username, password, adminBool, uid, funds, add):
        cursor = self.cnx.cursor()
        insertRow = "UPDATE users SET "
        execute = False
        inputList = []
        if username != "":
            insertRow += "username = %s, "
            execute = True
            inputList.append(username)
        if password != "":
            insertRow += "password = %s, "
            execute = True
            inputList.append(password)
        if adminBool != "":
            insertRow += "admin = %s, "
            execute = True
            inputList.append(adminBool)
        if funds != "":
            if add:
                try: #If add is true, such as when purchasing, add the new value to the old one
                    oldfunds = self.readRows.readUserFunds(uid)
                    funds = float(oldfunds) + float(funds)
                except Exception as e: 
                    print("Invalid user input")
                    #print(e)
                    return False
            insertRow += "funds = %s, "
            execute = True
            inputList.append(funds)

        if execute:#If none of the fields have updated values, then don't execute
            try:
                insertRow = insertRow[:-2] #Remove the last ", "
                insertRow += " WHERE uid = %s"
                inputList.append(uid)
                cursor.execute(insertRow, inputList)
                self.cnx.commit()
                self.logger.info("Updated user in the users table")
            except Exception as e: 
                print("Update input was invalid")
                self.logger.info("Failed to update user in the users table")
                #print(e)
                return False
        return True

    def updateBooksRow(self, bookname, author, release, price, amount, bid, subtract):
        cursor = self.cnx.cursor()

        insertRow = "UPDATE books SET "
        execute = False
        inputList = []
        if bookname != "": #Input of "" indicates to keep it the same
            insertRow += "bookname = %s, "
            execute = True
            inputList.append(bookname)
        if author != "":
            insertRow += "author = %s, "
            execute = True
            inputList.append(author)
        if release != "":
            insertRow += "release_year = %s, "
            execute = True
            inputList.append(release)
        if price != "":
            insertRow += "price = %s, "
            execute = True
            inputList.append(price)
        if amount != "":
            if subtract:
                try: #If subtract is true, such as when purchasing, subtract the new value from the old one
                    oldAmount = self.readRows.readBookAmount(bid)
                    amount = int(oldAmount) - int(amount)
                except Exception as e: 
                    print("Invalid book input")
                    #print(e)
                    return False
            insertRow += "amount = %s, "
            execute = True
            inputList.append(amount)

        if execute:#If none of the fields have updated values, then don't execute
            try:
                insertRow = insertRow[:-2] #Remove the last ", "
                insertRow += " WHERE bid = %s"
                inputList.append(bid)
                cursor.execute(insertRow, inputList)
                self.cnx.commit()
                self.logger.info("Updated book in the books table")
            except Exception as e: 
                print("Invalid book input")
                self.logger.info("Failed to update book in the books table")
                #print(e)
                return False
        return True
        
    def updateOrdersRow(self, uid, bid, date, purchases, oid, spent):
        cursor = self.cnx.cursor()

        insertRow = "UPDATE orders SET "
        execute = False
        inputList = []
        if uid != "": #Input of "" indicates to keep it the same
            insertRow += "uid = %s, "
            execute = True
            inputList.append(uid)
        if bid != "":
            insertRow += "bid = %s, "
            execute = True
            inputList.append(bid)
        if date != "":
            if date == "1":
                date = datetime.now()
            else:
                date = self.insertRows.inputDate() 
            date = date.strftime("%Y-%m-%d %H:%M:%S")
            insertRow += "orderTime = %s, "
            execute = True
            inputList.append(date)
        if purchases != "":
            insertRow += "purchases = %s, "
            execute = True
            inputList.append(purchases)
        if spent != "":
            insertRow += "spent = %s, "
            execute = True
            inputList.append(spent)

        if execute:#If none of the fields have updated values, then don't execute
            try:
                insertRow = insertRow[:-2] #Remove the last ", "
                insertRow += " WHERE oid = %s"
                inputList.append(oid)
                cursor.execute(insertRow, inputList)
                self.cnx.commit()
                self.logger.info("Updated order in the orders table")
            except Exception as e: 
                print("Invalid order input")
                self.logger.info("Failed to update order in the orders table")
                #print(e)
                return False
        return True
        