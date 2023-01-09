import mysql.connector
from mysql.connector import MySQLConnection, Error

def getConnection():

    khaibao = mysql.connector.connect(host='localhost',
                                    user='root',
                                    passwd='root',
                                    database='Quanlynhansu')
    return khaibao
    