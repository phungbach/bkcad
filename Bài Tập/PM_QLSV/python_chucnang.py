#tạo các chức năng
from pythonclass import Person

listhocvien = []
class Quanlylop:
    def create_hoc_vien(self): 
        n = int(input("nhap so luong hoc vien"))
        i = 0
        while(i < n):
            i += 1 #lap vo han
            id = int(input("Nhap id: "))
            name = input("Nhap ten: ") 
            age = int(input("Nhap tuoi: "))
            country = input("Nhap nuoc: ")
            information =  input("Nhap thong tin: ") 
            hocvien = Person(id,name,age,country,information)
            self.listhocvien.append(hocvien)

    def show_hocvien(self): #show hoc vien
        for i in self.listhocvien:
            print(i.id,i.name,i.age,i.country,i.information,sep=" - ")

#update

#delete

hocvien = Quanlylop()
hocvien.create_hoc_vien()
hocvien.show_hocvien()