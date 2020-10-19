import mysql.connector as sql

my_db = sql.connect(
    host="localhost",
    user="root",
    passwd="varun"
)
print("connected")

cursor = my_db.cursor()

try:
    cursor.execute("create database testpython")
except:
    print("db exists")

cursor.execute("use testpython")

try:
    cursor.execute("create table testsudoku(zero int,one int,two int,three int,four int,five int,six int,seven int,"
                   "eight int)")
except:
    print("table exists")

c = "insert into testsudoku(zero,one,two,three,four,five,six,seven,eight) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
v = [0, 1, 2, 3, 4, 5, 6, 7, 8]
cursor.execute(c,v)
my_db.commit()

cursor.execute("select * from testsudoku")
print(cursor.fetchall())

cursor.execute("drop table testsudoku")
my_db.commit()

try:
    cursor.execute("select * from testsudoku")
    print(cursor.fetchall())
except:
    print("table does not exist")
