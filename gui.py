
from msilib.schema import tables
from re import I
import sqlite3
import os
import sys
from tkinter import N

data = sqlite3.connect("D:/test/EpilogJobManagement.db3-first.db3")

cursor = data.cursor()

table = "Configuration"
sql = "PRAGMA table_info(" + table + ")"

cursor.execute(sql)
results = cursor.fetchall()

i = 0
while i < len(results):
    if results[i][1] == "ID":
        print(i)
    i += 1
