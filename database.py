from re import I
import sqlite3


def readDatabase(filePath):
    conn = sqlite3.connect(filePath)
    cur = conn.cursor()
    return cur

def checkDupilcate():
    pass

def checkId():
    pass

def merge(table1, table2):
    combined = set(table1) | set(table2)
    return combined

def getAllTableNames(cursor):

    sql="SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(sql)
    tables = cursor.fetchall()
    return tables

def getIDIndex(columnList):

    i = 0
    while i < len(columnList):
        if columnList[i] == "ID":
            return i
        i += 1 

def getColunmNames(cursor, tableName):
    
    sql = "PRAGMA table_info(" + tableName + ")"

    cursor.execute(sql)
    columnsInfo = cursor.fetchall()

    columnsList = []

    for column in columnsInfo:
        columnsList.append(column[1])
    return columnsList

def main():
    cur1 = readDatabase("D:/test/EpilogJobManagement.db3-first.db3")
    cur2 = readDatabase("D:/test/EpilogJobManagement.db3-second.db3")
    table1 = getAllTableNames(cur1)
    table2 = getAllTableNames(cur2)
    if table1 != table2:
        print("The tables are different!")
        exit()

    num_tables = len(table1)

    for i in range(num_tables):
        # the name of the table we are going to merge
        temp_table_name = table1[i][0]
        #print(temp_table_name)
        if temp_table_name != "sqlite_sequence":

            # get all the columns name of this table
            temp_columns_list = getColunmNames(cur1, temp_table_name)
            #print(temp_columns_list)
            # get the index of ID column of this table
            ID_index = getIDIndex(temp_columns_list)
            print(ID_index)



            # start merging
            sql = "SELECT * FROM " + temp_table_name
            cur1.execute(sql)
            result1 = cur1.fetchall() # all the rows in table1
            cur2.execute(sql)
            result2 = cur2.fetchall() # all the rows in table2

            # temp_result = result1 + result2
            







if __name__ == "__main__":
    main()