from datetime import datetime
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien

class DanhSachSv:
    def __init__(self):
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    # tìm sinh viên theo mssv , nếu có trả về sinh viên 
    def timSvTheoMs(self, mssv: int) -> list:
        return [sv for sv in self.dssv if sv.mssv == mssv]

    # tìm sinh viên theo mssv,  nếu có trả về vị trí của sinh viên trong danh sách
    def timVTSvTheoMssv(self, mssv: int) -> int:
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]

    def timSvTheoTrinhDo(self, trinhDo: str, date: str):
        return [sv for sv in self.timSvSinhTruocNgay(datetime.strptime(date, "%d/%m/%Y")) if isinstance(sv, SinhVienPhiCQ) and sv.trinhDo == trinhDo ]
    
    # Tim sinh vien co diem ren luyen tu 80 tro len
    def timSvTheoDRL(self, diem: int):
        return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv.diemRL >= diem]
    
    
    #Xoa mssv, cho biet co xoa duoc hay khong
    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    #Tim tat ca sinh vien sinh truoc 15/8/2000
    def timSvSinhTruocNgay(self, ngay: datetime) -> list:
        return [sv for sv in self.dssv if sv._ngaySinh<ngay]
       
    #Tim tat ca sinh vien ten Nam trong danh sach
    def timSvTheoTen(self, ten: str) -> list:
        return [sv for sv in self.dssv if(sv.hoTen.split(" ")[-1].upper()== ten.upper())]
    
    #Doc dssv tu file 
    def readFile(self, fileName: str):
        f = open(fileName, 'r', encoding="utf8")
        lines = f.readlines()
        for line in lines:
            sp = line.split("*")
            sv = SinhVien(sp[0],sp[1],sp[2])
            self.themSV(sv)
        return self.dssv
    
    def sortByName(self, type: str):
        if(type == "TANG"):
            for i in range(len(dssv.dssv) - 1):
                for j in range(i+1, len(dssv.dssv)):
                    if(dssv.dssv[i].hoTen.split(" ")[-1].upper() > dssv.dssv[j].hoTen.split(" ")[-1].upper()):
                        dssv.dssv[i], dssv.dssv[j] = dssv.dssv[j], dssv.dssv[i]
        return dssv.xuat()    
            
    # sv1 = SinhVien(1957690, "Nguyễn Văn A", datetime.strptime("1/1/2000", "%d/%m/%Y"))
    # sv2 = SinhVien(1957690, "Nguyễn Văn Nam", datetime.strptime("2/2/1997", "%d/%m/%Y"))

dssv = DanhSachSv()
# dssv.readFile(fileName='sinhvien.txt')
# dssv.sortByName("TANG")
    # dssv.themSV(sv1)
    # dssv.themSV(sv2)
    # dssv.xuat()
    # ms = "1967690"
    # kq = dssv.timSvTheoMssv(ms)

    # vt = dssv.timVTSvTheoMssv(ms)
    # if vt != -1:
    #     print(f"Sinh vien co ma so {ms} nam o vi tri thu {vt + 1} trong danh sach")
    # else:
    #     print(f"Sinh vien co ma so {ms} khong ton tai trong danh sach")

    # if dssv.xoaSvTheoMssv(ms):
    #     print(f"Da xoa sinh vien co ma so {ms} trong danh sach")
    # else:
    #     print(f"Khong xoa duoc vi mssv {ms} khong ton tai trong danh sach")

    # kq = dssv.timSvSinhTruocNgay(datetime.strptime("1/1/2000", "%d/%m/%Y"))
    # print(kq)


    # kq2 = dssv.timSvTheoTen("Nam")
    # print(" danh sach sinh vien ten Nam ",kq2)