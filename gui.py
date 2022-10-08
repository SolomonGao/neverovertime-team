
from msilib.schema import tables
import sqlite3
import os
import sys
from tkinter import N

data = sqlite3.connect("D:/test/EpilogJobManagement.db3-first.db3")

cursor = data.cursor()

table = "jobSubCategories"
sql = "PRAGMA table_info(" + table + ")"

cursor.execute(sql)
results = cursor.fetchall()

print(results)