from py_class import Persion

class Quanlynhanvien:
    listnhanvien = []
    lst_so = [0,1,2]
 
    def create_nhanvien(self):
        try:
            n = int(input("Nhập số học viên: "))
        except:
                print("Vui lòng nhập số!")
        i = 0
        while (i < n):
            i += 1
            id = ''
            ten = input("Nhập Tên: ")
            try:
                tuoi = int(input("Nhập Tuổi: "))
            except:
                print("Vui lòng nhập số!")
            quequan = input("Nhập quê quán: ")
            chucvu = input("Nhập GD-Giám Đốc TP-Trưởng Phòng CB-Cán Bộ: ")
            try:
                gioitinh = int(input("Nhập 0-Unknow 1-Male 2-Famale: "))
                if gioitinh != self.lst_so:
                    print("Vui lòng chọn 0 or 1 or 2") 
                chamcong = int(input("Chấm công: "))
            except:
                print("Vui lòng nhập số!")
            nhanvien = Persion(id,ten,tuoi,quequan,chucvu,gioitinh,chamcong)

            a = 1
            nhanvien.id = nhanvien.chucvu + str(a)
            for j in self.listnhanvien:
                if(j.id == nhanvien.id):
                    a += 1
                    nhanvien.id = nhanvien.chucvu + str(a)
            

            if nhanvien.chucvu == 'GD':
                nhanvien.chucvu = 'Giám Đốc'
                nhanvien.tienluong = float(chamcong * 1000000)
            elif nhanvien.chucvu == 'TP':
                nhanvien.chucvu = 'Trưởng Phòng'
                nhanvien.tienluong = float(chamcong * 500000)
            elif nhanvien.chucvu == 'CB':
                nhanvien.chucvu = 'Cán Bộ'
                nhanvien.tienluong = float(chamcong * 400000)

            if nhanvien.gioitinh == '0':
                nhanvien.gioitinh = 'Unknow'
            elif nhanvien.gioitinh == '1':
                nhanvien.gioitinh = 'Male'
            elif nhanvien.gioitinh == '2':
                nhanvien.gioitinh = 'Famale'
            
            self.listnhanvien.append(nhanvien)


    def update_nhanvien(self,id1):
        for i in self.listnhanvien:
            if(i.id == id1):
                ten = input("Nhập tên: ")
                try:
                    tuoi = int(input("Nhập Tuổi: "))
                except:
                    print("Vui lòng nhập số!")
                quequan = input("Nhập quê quán: ")
                chucvu = input("Nhập chức vụ: ")
                try:
                    gioitinh = int(input("Nhập giới tính: "))
                    if gioitinh != self.lst_so:
                        print("Vui lòng chọn 0 or 1 or 2") 
                    chamcong = int(input("Chấm công: "))
                except:
                    print("Vui lòng nhập số!")
                i.ten = ten
                i.tuoi = tuoi
                i.quequan = quequan
                i.chucvu = chucvu
                i.gioitinh = gioitinh
                i.chamcong = chamcong

    def delete_nhanvien(self,id2):
        for i in self.listnhanvien:
            if(i.id == id2):
                self.listnhanvien.remove(i)

    def show_nhanvien(self):
        for i in self.listnhanvien:
            print(i.id," - ",i.ten," - ",i.tuoi," - ",i.quequan," - ",i.chucvu," - ",i.gioitinh," - ",i.chamcong," - ",i.tienluong,"đ")

    def sapxep_nhanvien(self):
        self.listnhanvien.sort(key=lambda x:x.name, reverse=False)

