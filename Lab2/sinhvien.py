from datetime import datetime


class SinhVien:
    # biến của lớp , chúng cho tất cả đối tượng thuộc lớp
    truong = "Đại học Đà Lạt"
    
    # hàm khởi tạo, hàm tạo lập : khởi gán các thuộc tính của đối tượng
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime):
        self._maSo = maSo #thuộc tính private
        self._hoTen = hoTen #thuộc tính private
        self._ngaySinh = ngaySinh #thuộc tính private
        
    #cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSo
    @property
    def maSo(self):
        return self._maSo
    
    # cho phép thay đổi giá trị của thuộc tính maSo
    @maSo.setter
    def maSo(self, maso):
        if self.laMsHopLe(maso):
            self._maSo = maso
    # phương thức tĩnh : các phương thức không truy xuất gì đến thuộc tính , hành vi của lớp
    # những phương thức này không cần truyền tham số mặc định self
    # đây không phải là một hành vi ( phương thức ) của 1 đối tượng thuộc lớp
    @staticmethod
    def laMsHopLe(self, maso: int):
        return len(str(maso)) == 7
    # phương thức của lớp , chỉ truy xuất tới các biến thành viên của lớp
    # không truy xuất được các thuộc tính riêng của đối tượng

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong =tenmoi
    
    #tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"

    # hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")
        
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
        return [sv for sv in self.dssv if sv.ngaySinh<ngay]
       
    #Tim tat ca sinh vien ten Nam trong danh sach
    def timSvTheoTen(self, ten: str) -> list:
        return [sv for sv in self.dssv if(sv.hoTen.split(" ")[-1].upper()== ten.upper())]
            
            
    sv1 = SinhVien(1957690, "Nguyễn Văn A", datetime.strptime("1/1/2000", "%d/%m/%Y"))
    sv2 = SinhVien(1957690, "Nguyễn Văn Nam", datetime.strptime("2/2/1997", "%d/%m/%Y"))

    dssv = dssv()
    dssv.themSV(sv1)
    dssv.themSV(sv2)
    dssv.xuat()
    ms = "1967690"
    kq = dssv.timSvTheoMssv(ms)

    vt = dssv.timVTSvTheoMssv(ms)
    if vt != -1:
        print(f"Sinh vien co ma so {ms} nam o vi tri thu {vt + 1} trong danh sach")
    else:
        print(f"Sinh vien co ma so {ms} khong ton tai trong danh sach")

    if dssv.xoaSvTheoMssv(ms):
        print(f"Da xoa sinh vien co ma so {ms} trong danh sach")
    else:
        print(f"Khong xoa duoc vi mssv {ms} khong ton tai trong danh sach")

    kq = dssv.timSvSinhTruocNgay(datetime.strptime("1/1/2000", "%d/%m/%Y"))
    print(kq)


    kq2 = dssv.timSvTheoTen("Nam")
    print(" danh sach sinh vien ten Nam ",kq2)