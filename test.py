
import sqlite3
import os
import sys
from tkinter import N

data = sqlite3.connect("D:/test/EpilogJobManagement.db3-first.db3")

cursor = data.cursor()

cursor.execute("SELECT * FROM jobSubCategories")
results = cursor.fetchall()

# for result in results:
#     print(result)



data2 = sqlite3.connect("D:/test/EpilogJobManagement.db3-second.db3")

cursor1 = data2.cursor()

cursor1.execute("SELECT * FROM jobSubCategories")
results2 = cursor1.fetchall()

# target = set(results) | set(results2)

target = results + results2

des_conn = sqlite3.connect("test.db3")
des_cur = des_conn.cursor()

n = 1
temp_list = []
for a in target:
    # id
    id = a[0:1][0]
    # name
    name = a[1:2][0]
    # sortID
    sortID = a[2:3][0]
    temp_list.append((n, name, sortID))
    n += 1


for temp in temp_list:
     print(temp)
    

temp_sql = ""
temp_data_list = results
table = "jobSubCategories"

id = "ID"
name = "name"
sortID = "SortID"

column = [id, name, sortID] 

dic = {
    type(int) : "INT",
    type(str) : "TEXT",
    "Picture" : "BLOB"
 }

column = "( " 
n = 0

len(column)

# while n < len(column):
#     column += "1"
#     n += 1
#     print(n)



# sql = "CREATE TABLE IF NOT EXISTS " + table + " ( " + id + " "\
# + type(id) + "PRIMARY KEY, " + name + " " + type(name) + \
#  + sortID + " " + type(sortID)

# des_cur.execute(sql)

# for a in temp_list:

#     des_cur.execute('INSERT OR IGNORE INTO jobSubcategories (ID, name, SortID) VALUES(?, ?, ?)', (a[0], str(a[1]), a[2]))

des_conn.commit()

# conn = sqlite3.connect('test_database') 
# c = conn.cursor()

# c.execute('''
#           CREATE TABLE IF NOT EXISTS products
#           ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
#           ''')
          
# c.execute('''
#           CREATE TABLE IF NOT EXISTS prices
#           ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
#           ''')
                     
# conn.commit()