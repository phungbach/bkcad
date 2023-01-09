#THUC THI CAC CHUC NANG

#MENU

from py_func import *

hocvien = Quanlynhanvien()

def main_QLNV():
    while(True):
            print("-------------------------------")
            print("1. Thêm nhân viên")
            print("2. Hiển thị nhân viên")
            print("3. Sửa thông tin nhân viên")
            print("4. Xóa thông tin nhân viên")
            print("5. Sắp xếp nhân viên")
            print("6. Thoát")
            print("-------------------------------")

            print("Moi ban chon chuc nang")
            lst_so = [1,2,3,4,5,6]
            try:
                
                nhap = int(input("Chon chuc nang: "))
                if nhap != lst_so:
                    print("-------------------------------")
                    print("Vui lòng nhập số đúng số!")
                    print("-------------------------------")
                elif (nhap == 1):
                    hocvien.create_nhanvien()
                elif (nhap == 2):
                    hocvien.show_nhanvien()
                elif (nhap ==3):
                    id1 = int(input("Nhap id muon sua: "))
                    hocvien.update_nhanvien(id1)
                    print("Da sua thanh cong")
                elif (nhap ==4):
                    id2 = int(input("Nhap id muon xoa: "))
                    hocvien.delete_nhanvien(id2)
                    print("Da xoa thanh cong")
                elif (nhap ==5):
                    hocvien.sapxep_nhanvien()
                    hocvien.show_nhanvien()
                elif (nhap ==6):
                    break
            except:
                print("-------------------------------")
                print("Vui lòng nhập đúng giá trị!")
                print("-------------------------------")

main_QLNV()