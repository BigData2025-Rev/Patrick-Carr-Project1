import logging
class Tables:
    cnx = None
    logger = logging.getLogger()

    def __init__(self, cnx, logger):
        self.cnx = cnx
        self.logger = logger

    #users table fields:
    # uid int, also the primary key
    # username varchar
    # password varchar
    # admin BOOLEAN
    def createUsersTable(self):
        cursor = self.cnx.cursor()
        self.logger.info("Creating users table if it does not exist")
        createTable = "CREATE TABLE IF NOT EXISTS users(uid int AUTO_INCREMENT not null, username varchar(30) unique not null, " 
        createTable +="password varchar(30) unique not null, admin boolean, PRIMARY KEY (uid), funds float not null CHECK(funds>-1))"
        cursor.execute(createTable)


    #books table fields:
    # bid int, also the primary key
    # bookname varchar
    # author varchar
    # release_year year
    # price float
    # amount int
    #Two different books could have the same name or author, so those do not have the unique constraint
    def createBooksTable(self):
        cursor = self.cnx.cursor()
        self.logger.info("Creating books table if it does not exist")
        createTable = "CREATE TABLE IF NOT EXISTS books(bid int AUTO_INCREMENT not null, bookname varchar(50) not null , " 
        createTable +="author varchar(50) not null, release_year year, price float not null CHECK(price>-1), amount int CHECK(amount>-1), PRIMARY KEY (bid))"
        cursor.execute(createTable)

    #orders table fields:
    # oid int, also the primary key
    # uid int, foreign key from users
    # bid int, foreign key for books
    # orderTime datetime
    # purchases int
    def createOrdersTable(self):
        cursor = self.cnx.cursor()
        self.logger.info("Creating orders table if it does not exist")
        createTable = "CREATE TABLE IF NOT EXISTS orders(oid int AUTO_INCREMENT not null, uid int not null, bid int not null, orderTime datetime, purchases int CHECK(purchases>0), "
        createTable += "PRIMARY KEY (oid), FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE, FOREIGN KEY (bid) REFERENCES books (bid) ON DELETE CASCADE, spent float not null CHECK(spent>-1))"
        cursor.execute(createTable)
