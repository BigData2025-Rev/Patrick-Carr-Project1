#Admin Only
#import re
from datetime import datetime

class InsertRows:
    cnx = None
    def __init__(self, cnx):
        self.cnx = cnx

    #users table fields:
    # uid int, also the primary key [0]
    # username varchar [1]
    # password varchar [2]
    # admin BOOLEAN [3]
    # funds float[4]
    def insertUserRow(self, username, password, adminBool, funds):   
        cursor = self.cnx.cursor()

        insertRow = "INSERT INTO users (username, password, admin, funds) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(insertRow, (username, password, adminBool, funds))
            self.cnx.commit()
            return True
        except Exception as e: 
            print("Invalid user input")
            #print(e)
        return False
      
    #books table fields: 
    # bid int, also the primary key [0]
    # bookname varchar [1]
    # author varchar [2]
    # release_year year [3]
    # price float [4]
    # amount int [5]
    #Two different books could have the same name or author, so those do not have the unique constraint
    def insertBookRow(self, bookname, author, release, price, amount):
        cursor = self.cnx.cursor()

        insertRow = "INSERT INTO books (bookname, author, release_year, price, amount) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(insertRow, (bookname, author, release, price, amount))
            self.cnx.commit()
            return True            
        except Exception as e: 
            print("Invalid book input")
            #print(e)
        return False
        
    
    #orders table fields:
    # oid int, also the primary key
    # uid int, foreign key from users
    # bid int, foreign key for books
    # orderTime datetime
    # purchases int
    def insertOrderRow(self, uid, bid, dateInput, purchases, spent):
        if dateInput == "1":
            date = datetime.now()
        else:
            date = self.inputDate() 
        date = date.strftime("%Y-%m-%d %H:%M:%S")

        cursor = self.cnx.cursor()
        insertRow = "INSERT INTO orders (uid, bid, orderTime, purchases, spent) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(insertRow, (uid, bid, date, purchases, spent))
            self.cnx.commit()
            return True
        except Exception as e: 
            print("Invalid order input")
            #print(e)
        return False
        
    def inputDate(self):
        months = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
        loop = True
        while loop:
            loop = False
            year = input("Input year number:")
            month = input("Input month:")
            if month.lower() in months:#Convert month input into a number
                month = months[month.lower()]
            day = input("Input day number:")
            hour = input("Input hour number:")
            minute = input("Input minute number:")
            second = input("Input second number:")
            try:
                date = datetime(int(year),int(month),int(day),int(hour),int(minute),int(second))
            except Exception as e: 
                print("Invalid date & time")
                #print(e)
                loop = True
        return date

        
        
