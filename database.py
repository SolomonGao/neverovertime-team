import sqlite3

# The function gets the file path and connects it to the sqlite3 and returns the curosr.
def readDatabase(filePath):
    conn = sqlite3.connect(filePath)
    cur = conn.cursor()
    return cur

# The function merges two set into one (No duplicate) and returns it.
def merge(table1, table2):
    combined = set(table1) | set(table2)
    return combined

# This function returns all the table names in the database.
def getAllTableNames(cursor):

    sql="SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(sql)
    tables = cursor.fetchall()
    return tables

# This function returns the ID indext of one selected table.
def getIDIndex(columnDic):

    n = 0
    for key in columnDic.keys():
        if key == "ID":
            return n
        n += 1

# This function forms a sql command that stores all the columns names and data types and returns it.
# Format :  ( column name datatype PRIMARY KEY(if applied), column name data type, .... ) (based on the length)
def SqlSentenceForColumn(columnNameDic):
    sentence = " ( "
    n = 0
    for k, v in columnNameDic.items():
        if k != "ID":
            if n != len(columnNameDic) - 1:
                sentence += k + " " + v + ", "
            else:
                sentence += k + " " + v + " )"
        else:
            if n != len(columnNameDic) - 1:
                sentence += k + " " + v + " PRIMARY KEY " + ", " 
            else:
                sentence += k + " " + v + " PRIMARY KEY " + ")" 

        n += 1
    return sentence

# This function returns a dictionary. The key is the column name and the value is the data type in sql.
def getColunmNames(cursor, tableName):
    
    sql = "PRAGMA table_info(" + tableName + ")"

    cursor.execute(sql)
    columnsInfo = cursor.fetchall()

    columnsDic = dict()
    for column in columnsInfo:
        columnsDic[column[1]] = column[2]

    return columnsDic

# This function reorders the ID for the merged table and return it.
def reorderID(IDIndex, data):

    j = 1
    temp_list = []
    for datum in data:
        temp = []
        for i in range(len(datum)):
            if i != IDIndex:
                temp.append(datum[i])
            else:
                temp.append(j)
        temp_list.append(temp)
        j += 1
    return temp_list

# This function creates a new table in the new database.
def createTables(targetConn, tableName, columnsDic):
    # the sql command to create table
    column_sentence = SqlSentenceForColumn(columnsDic)
    sql_creating = "CREATE TABLE IF NOT EXISTS " + tableName + column_sentence
    # print(sql_creating)

    target_cur = targetConn.cursor()
    target_cur.execute(sql_creating)

# This function forms a sql command for insertion. 
# Format :  INSERT OR IGNORE INTO "table name" (?, ?, ?, ....)(based on the length)
def sqlSentenceForInsertion(tableName, columnNameDic):

    table = tableName + "("
    value = " VALUES("
    n = 0
    for key in columnNameDic.keys():
        if n != len(columnNameDic) - 1:
            table += key +", "
            value += "?, "
        else:
            table += key +")"
            value += "?)"
        n += 1

    sql = "INSERT OR IGNORE INTO " + table + value
    return sql

# This function inserts a row into a selected table 
def insertValue(targetConn, tableName, columnsDic, values):
    # the sql command to insert row in to a table
    sql = sqlSentenceForInsertion(tableName, columnsDic)

    target_cur = targetConn.cursor()
    target_cur.execute(sql, values)

def main():
    # two databases we are going to merge
    cur1 = readDatabase("D:/test/EpilogJobManagement.db3-first.db3")
    cur2 = readDatabase("D:/test/EpilogJobManagement.db3-second.db3")
    # target database
    target_conn = sqlite3.connect("test.db3")
    table1 = getAllTableNames(cur1)
    table2 = getAllTableNames(cur2)
    # The tables should be exactly the same in order to use the program 
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
            temp_columns_dic = getColunmNames(cur1, temp_table_name)
            # print(temp_columns_list)
            # get the index of ID column of this table
            ID_index = getIDIndex(temp_columns_dic)
            # Create all the table in the new database
            createTables(target_conn, temp_table_name, temp_columns_dic)
            # start merging
            sql = "SELECT * FROM " + temp_table_name
            cur1.execute(sql)
            result1 = cur1.fetchall() # all the rows in table1
            cur2.execute(sql)
            result2 = cur2.fetchall() # all the rows in table2
            # temp_result = set(result1) | set(result2)
            temp_result = result1 + result2
            # reorder the id index
            orderedRows = reorderID(ID_index, temp_result)
            # loop the data in the table
            for row in orderedRows:
                tempValue = []
                for value in row:
                    tempValue.append(value)
                tempValue = tuple(tempValue)
                insertValue(target_conn, temp_table_name, temp_columns_dic, tempValue)

            target_conn.commit()

if __name__ == "__main__":
    main()