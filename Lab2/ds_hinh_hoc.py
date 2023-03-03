from cgitb import reset
import sys
from hinhChuNhat import HinhChuNhat
from hinhhoc import HinhHoc
from hinhtron import HinhTron
from hinhvuong import HinhVuong
from loaiHinh import LoaiHinh

class DanhSachHH:
    def __init__(self):
        self.dshh = []

    def themHH(self, hh: HinhHoc):
        self.dshh.append(hh)

    def xuat(self):
        for hh in self.dshh:
            print(hh)

    def readFile(self, fileName: str):
        f = open(fileName, 'r', encoding="utf8")
        lines = f.readlines()
        for line in lines:
            sp = line.split("*")
            if(sp[0] == "HinhVuong"):
                hv = HinhVuong(float(sp[1]))
                self.themHH(hv)
            elif(sp[0] == "HinhChuNhat"):
                hcn = HinhChuNhat(float(sp[1]), float(sp[2]))
                self.themHH(hcn)
            elif(sp[0] == "HinhTron"):
                ht = HinhTron(float(sp[1]))
                self.themHH(ht)
        return self.dshh

    def timHinhCoDienTichLonNhat(self):
        max = 0
        result = HinhHoc(0)
        for hh in self.dshh:
            if(hh.dienTich > max):
                max = hh.dienTich
                result = hh
        return print(result)

    def timHinhCoDienTichNhoNhat(self):
        min = sys.maxsize
        result = HinhHoc(0)
        for hh in self.dshh:
            if(hh.dienTich < min):
                min = hh.dienTich
                result = hh
        return print(result)

    def timHinhCoDienTichLonNhatTheoLoai(self, loaiHinh: str):
        max = 0
        result = HinhHoc(0)
        if(loaiHinh == 'HinhTron'):
            for hh in self.dshh:
                if(hh.dienTich > max and isinstance(hh, HinhTron)):
                    max = hh.dienTich
                    result = hh
        elif(loaiHinh == 'HinhVuong'):
            for hh in self.dshh:
                if(hh.dienTich > max and isinstance(hh, HinhVuong)):
                    max = hh.dientich
                    result = hh
        elif(loaiHinh == 'HinhChuNhat'):
            for hh in self.dshh:
                if(hh.dienTich > max and isinstance(hh, HinhChuNhat)):
                    max = hh.dienTich
                    result = hh
        return print(result)

    def sapXepTheoDienTich(self):
        return self.dshh.sort(key = lambda x: x.dienTich, reverse = True)

    def demSoLuongHinhTheoLoai(self, loai: str):
        result = []
        if(loai == "HinhTron"):
            result = [hh for hh in self.dshh if isinstance(hh, HinhTron)]
        if(loai == "HinhVuong"):
            result = [hh for hh in self.dshh if isinstance(hh, HinhVuong)]
        if(loai == "HinhChuNhat"):
            result = [hh for hh in self.dshh if isinstance(hh, HinhChuNhat)]
        return f"Co {len(result)} {loai}"

    def tinhTongDienTich(self):
        sum = 0
        for hh in self.dshh:
            sum += hh.dienTich
        return f"Tong dien tich cac hinh la {sum}"

    def timViTriCuaHinh(self, h: HinhHoc):
        for hh in self.dshh:
            if(isinstance(hh, h) and hh.canh == h.canh):
                return hh

    def timHinhTheoDienTich(self, s: float):
        return [hh for hh in self.dshh if(hh.dienTich == s)]

    def xoa(self, hh: HinhHoc):
        self.dshh.remove(hh)