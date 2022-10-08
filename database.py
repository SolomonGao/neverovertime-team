import sqlite3

sql_inqury_tables="SELECT name FROM sqlite_master WHERE type='table'"

def readDatabase(filePath):
    pass

def checkDupilcate():
    pass

def checkId():
    pass

def merge(table1, table2):
    combined = set(table1) | set(table2)
    return combined


def sql_modify(table_info_unmod):
    k=0
    table_info_modified="("
    while k<len(table_info_unmod):
        table_info_modified = table_info_modified+table_info_unmod[k][1]+" "+table_info_unmod[k][2]+","
        k+=1
    table_info_modified=table_info_modified[0:-1]+")"
    return  (table_info_modified)

def compare_tables(tables_cur_db3,tables_des_db3,con_current_db3,con_des_db3):
    j=0
    while j<len(tables_cur_db3):
        if (not tables_cur_db3[j] in tables_des_db3) and (str(tables_cur_db3[j])[3:-3]!='sqlite_sequence'):
            con_current_db3_cursor=con_current_db3.cursor()
            con_current_db3_cursor.execute("PRAGMA table_info ("+str(tables_cur_db3[j])[3:-3]+")")
            table_info_modified=sql_modify(con_current_db3_cursor.fetchall())
            con_des_db3_cursor=con_des_db3.cursor()
            new_table_sql="create table "+ str(tables_cur_db3[j])[3:-3] + table_info_modified
            con_des_db3_cursor.execute(new_table_sql)         
            j+=1
        else: j+=1
    con_des_db3_cursor=con_des_db3.cursor()
    con_des_db3_cursor.execute(sql_inqury_tables)
    tables_des = con_des_db3_cursor.fetchall()
    con_des_db3.commit()


def append_data(con_current_data,con_des_data,tables_current_data):
    #把当前数据库的链接、目标数据库的链接、当前数据库的table列表同时传入
    print('\n' + ' is Beginning !')
    m=0
    cur_current_data=con_current_data.cursor()
    cur_des_data=con_des_data.cursor()
    while m<len(tables_current_data):
        if str(tables_current_data[m])[3:-3]!="sqlite_sequence":
            sql="select * from "+str(tables_current_data[m])[2:-3]
            cur_current_data.execute(sql)
            temp_data_list=cur_current_data.fetchall()
            temp_sql=""#用来存储插入记录信息，一次只能插入一个一维数组
            n=0
            if len(temp_data_list)>0:
                while n<len(temp_data_list[0]):#注意此处求取的长度是指二维数组有多少列，有它来决定？的个数
                    temp_sql+="?,"
                    n+=1
                temp_sql="("+temp_sql[0:-1]+")"#对循环后形成的"？,"列阵做修饰，去除尾部逗号，并加上括号来适配sql语句
                cur_des_data.executemany("insert into "+str(tables_current_data[m])[2:-3]+ " values " + temp_sql,temp_data_list)
                con_des_data.commit()
            print('\n'"-----"+str(tables_current_data[m])+"   Finished!")
            m+=1            
        else: m+=1
    print('\n'" All Tables Finished!")
    
def main():
    con_des=sqlite3.connect("D:/test/EpilogJobManagement.db3-second.db3")
    con_current = sqlite3.connect("D:/test/EpilogJobManagement.db3-first.db3")
    cur_current=con_current.cursor()    
    cur_current.execute(sql_inqury_tables)
    tables_current=cur_current.fetchall()
    cur_des=con_des.cursor()
    cur_des.execute(sql_inqury_tables)
    tables_des=cur_des.fetchall()

    compare_tables(tables_current,tables_des,con_current,con_des)
        #经过compare_tables函数后，目标数据库的表格已经大于等于当前待合并的数据库了
        #接下来逐个将表的信息录入目标数据库即可，因此再构建一个append_data函数
    append_data(con_current,con_des,tables_current)
    con_current.close()    

    print(tables_des)
    con_des.close()

main()