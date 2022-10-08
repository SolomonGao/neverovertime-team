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
        temp_table_name = table1[i][0]
        #print(temp_table_name)
        if temp_table_name != "sqlite_sequence":
            sql = "SELECT * FROM " + temp_table_name
            cur1.execute(sql)
            result1 = cur1.fetchall() # all the rows in table1
            cur2.execute(sql)
            result2 = cur2.fetchall() # all the rows in table2

            temp_result = result1 + result2
            print(len(temp_result))






if __name__ == "__main__":
    main()