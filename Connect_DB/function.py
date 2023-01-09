import pyclass
import mysql.connector

#kết nối giữa mysql và python
connect = pyclass.getConnection()
data = connect.cursor()

class Quanlylop:

    #C R U D

    def get_data():
        data.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
        ketqua = data.fetchall()
        for i in ketqua:
            return i
        connect.close()
        
    def get_data2():
        data.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
        ketqua = data.fetchone()
        while ketqua is not None:
            print(ketqua)
            ketqua = data.fetchone()

    def get_data_byid():
        data.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 2")
        ketqua = data.fetchall()
        for i in ketqua:
            print(i)

    def get_data_byid2():
        sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s"
        id = 3
        data.execute(sql,(id,))
        ketqua = data.fetchall()
        for i in ketqua:
            print(i)

    def get_data_byid_andage(id,age):
        sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s AND age = %s"
        # id = 3
        # age = 22
        data.execute(sql,(id,age))
        ketqua = data.fetchall()
        for i in ketqua:
            print(i)

    def create_data():
        sql = "INSERT INTO `Hocvien`(Id,`Name`,Age, Country	, English, Information)VALUES (5, 'Nguyen Van E' , 23, 'Da Nang',  3 , 4 )"
        data.execute(sql)
        connect.commit()
        print("Da them thanh cong")

    def update_data():
        sql = "UPDATE Quan_ly_hoc_vien.Hocvien SET Age = 25 WHERE Id = 5"
        data.execute(sql)
        connect.commit()
        print("Da cap nhat thanh cong")

    def delete_data():
        sql = "DELETE FROM Quan_ly_hoc_vien.Hocvien WHERE Country = 'Sai Gon' "
        data.execute(sql)
        connect.commit()
        print("Da xoa thanh cong")


    connect.close()
