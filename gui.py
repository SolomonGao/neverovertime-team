
from msilib.schema import tables
import sqlite3
import os
import sys
from tkinter import N
from database import reorderID

data = sqlite3.connect("D:/test/EpilogJobManagement.db3-first.db3")

cursor = data.cursor()

table = "Configuration"
sql = "SELECT * FROM " + table
cursor.execute(sql)
data = cursor.fetchall()


list = reorderID(0, data)

print(list)
# list = []
# id = 0
# j = 1
# temp_list = []
# for datum in data:
#     print(datum)
#     temp = []
#     for i in range(len(datum)):
#         if i != id:
#             temp.append(datum[i])
#         else:
#             temp.append(j)
#     temp_list.append(temp)
#     j += 1

