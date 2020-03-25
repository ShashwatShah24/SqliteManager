import sqlite3  
  
con = sqlite3.connect("Database01.db")  
print("Database opened successfully")  
  
con.execute("create table Table01 (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL,Password TEXT UNIQUE NOT NULL)")  
  
print("Table created successfully")  
  
con.close()