
from msilib.schema import tables
import sqlite3
import os
import sys
from tkinter import N

data = sqlite3.connect("D:/test/EpilogJobManagement.db3-first.db3")

cursor = data.cursor()

table = "jobSubCategories"
sql = "SELECT * FROM " + table
print(sql)
cursor.execute(sql)
data = cursor.fetchall()

list = []
id = 0
for datum in data:
    for i in range(len(datum)):
        temp = ()
    list.append()
