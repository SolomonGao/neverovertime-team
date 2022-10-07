
import sqlite3
import os
import sys


# import func1

# func1.func1()

data = sqlite3.connect("D:/test/EpilogJobManagement.db3-first.db3")

cursor = data.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
results = cursor.fetchall()

 # grab every table
print(results)

# # cursor.execute(f"SELECT * FROM {a}")
# # results1 = cursor.fetchall()
# # for result in results1:
# #    print(result)