from initialization import check
import mysql.connector
import pickle
import os
file_path = os.path.join("Bank-Management-System-Python-SQL-main", "src", "main", "OmJShah", "files", "firsttime.txt")
def cc():
    global cur
    global conn
    if not check.check():
        cred = open(file_path, "rb")
        dat=pickle.load(cred)
        cred.close()
        Passwo=dat[0]
        Databa=dat[1]
        conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
        cur=conn.cursor()
        return conn,cur
    else:
        return 0,0