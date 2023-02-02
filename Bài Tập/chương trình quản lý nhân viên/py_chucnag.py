# TAO CAC CHUC NANG LOP PYTHON
from py_class import Personnel

class Quanlynhansu:
    listnhansu = []

    # [A,C,D,E,F,G]

    def create_nhan_su(self):
            n = int(input("Nhap so hoc vien: "))
            i = 0
            while (i < n):
                i += 1 #Lap vo han
                id = self.autoID()
                ten = input("Nhap ten: ")
                tuoi = int(input("Nhap tuoi: "))
                diachi = input("Nhap dia chi: ")
                sodienthoai = int(input("Nhap so dien thoai: "))
                thongtin = input("Nhap thong tin them: ")
                diemdanhgia = int(input("Nhap diem danh gia: "))
                xeploai = ""
                nhansu = Personnel(id,ten,tuoi,diachi,sodienthoai,thongtin,diemdanhgia,xeploai)
                self.xeploaidanhgia(nhansu)
                self.listnhansu.append(nhansu)

    def show_nhan_su(self): 
        for i in self.listnhansu:
            print(i.id,i.ten,i.tuoi,i.diachi,i.sodienthoai,i.diemdanhgia,i.xeploai,sep=" - ")

    
    def update_nhan_su(self,id1):
        for i in self.listnhansu:
            if(i.id == id1):
                ten = input("Nhap ten: ")
                tuoi = int(input("Nhap tuoi: "))
                diachi = input("Nhap dia chi: ")
                sodienthoai = int(input("Nhap so dien thoai: "))
                thongtin = input("Nhap thong tin them: ")
                diemdanhgia = int(input("Nhap diem danh gia: "))
                xeploai = ""
                i.ten = ten
                i.tuoi = tuoi
                i.diachi = diachi
                i.sodienthoai = sodienthoai
                i.information = thongtin
                i.diemdanhgia = diemdanhgia
                i.xeploai = xeploai
        
                

    
    def delete_nhan_su(self,id2):
        for i in self.listnhansu:
            if(i.id == id2):
                self.listnhansu.remove(i)


    #Chức năng thêm

    #tạo id tăng dần
    def autoID(self):
        max = self.listnhansu.__len__() + 1
        return max

    #sắp xếp theo tên
    def sapxeptheoten(self):
        self.listnhansu.sort(key=lambda x: x.ten, reverse=False)

    #xep loai danh gia
    def xeploaidanhgia(self, ps:Personnel):
        if ps.diemdanhgia >= 8:
            ps.xeploai = "Gioi"
        elif ps.diemdanhgia >= 4:
            ps.xeploai = "Kha"
        else:
            ps.xeploai = "Yeu"
