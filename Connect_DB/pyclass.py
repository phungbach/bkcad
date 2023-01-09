import mysql.connector

def getConnection():
    khaibao = mysql.connector.connect(host='localhost',
                                    user='root',
                                    passwd='root',
                                    database='Quan_ly_hoc_vien')
    return khaibao

#pip3 install mysqlconnector