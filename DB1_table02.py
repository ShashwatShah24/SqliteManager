import sqlite3  
  
con = sqlite3.connect("Database01.db")  
print("Database opened successfully")  
  
con.execute("create table Table02 (id INTEGER PRIMARY KEY AUTOINCREMENT,Post TEXT NOT NULL,Password TEXT UNIQUE NOT NULL)")  
  
print("Table created successfully")  
  
con.close()