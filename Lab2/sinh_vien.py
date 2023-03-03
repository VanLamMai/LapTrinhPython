from datetime import datetime


class SinhVien:
    # biến của lớp , chúng cho tất cả đối tượng thuộc lớp
    truong = "Đại học Đà Lạt"
    # hàm khởi tạo, hàm tạo lập : khởi gán các thuộc tính của đối tượng
    def __init__(self, mssv: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = mssv #khai báo kiểu truy xuất là protected
        self._hoTen = hoTen 
        self._ngaySinh = ngaySinh 
        
    
    @property
    def hoTen(self):
        return self._hoTen
    
    @hoTen.setter
    def hoTen(self, hoTen: str):
        self._hoTen = hoTen
        
    @property
    def mssv(self):
        return self._maSo
    
    
    @mssv.setter
    def maSo(self, ms : int):
        if self.ktMsHopLe(ms):
            self._maSo = ms
    
    @staticmethod
    def ktMsHopLe(self, mssv: int):
        return len(str(mssv)) == 7
    
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"