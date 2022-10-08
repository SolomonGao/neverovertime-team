
import sqlite3
import os
import sys

data = sqlite3.connect("D:/test/EpilogJobManagement.db3-first.db3")

cursor = data.cursor()

cursor.execute("SELECT * FROM jobData")
results = cursor.fetchall()



data2 = sqlite3.connect("D:/test/EpilogJobManagement.db3-second.db3")

cursor1 = data2.cursor()

cursor1.execute("SELECT * FROM jobData")
results2 = cursor1.fetchall()

target = set(results) | set(results2)



