import sqlite3
con=sqlite3.connect('employee.db')
print("DataBase Connected")
cur=con.cursor()

con.execute('CREATE TABLE Employees(id integer primary key autoincrement,name TEXT,email TEXT,address TEXT)')

con.commit()
con.close()