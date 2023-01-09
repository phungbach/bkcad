from function import *

nhanvien = Quanlylop()

while(True):
    print("-------------------------------")
    print("1. Them nhan vien")
    print("2. Hiển thị nhân viên theo id")
    print("3. Hien thi nhan vien")
    print("4. Sua thong tin nhan vien")
    print("5. Xoa thong tin nhan vien")
    print("6. Sap Xep Theo Ten")
    print("-------------------------------")

    print("Moi ban chon chuc nang")

    nhap = int(input("Chon chuc nang: "))
    if (nhap == 1):
        nhanvien.create_data()
    elif (nhap == 2):
        nhanvien.get_data()
    elif (nhap == 3):
        nhanvien.get_data_byid()
    elif (nhap ==4):
        id1 = int(input("Nhap id muon sua: "))
        nhanvien.update_data()
        print("Da sua thanh cong")
    elif (nhap ==5):
        id2 = int(input("Nhap id muon xoa: "))
        nhanvien.delete_data()
        print("Da xoa thanh cong")
    #elif (nhap == 6):
        #nhanvien.sapxeptheoten()
        #print("Da sap xep thanh cong")
        #nhanvien.show_nhan_su()
    else:
        break


