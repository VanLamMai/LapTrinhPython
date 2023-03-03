from lib2to3.pgen2 import driver
from mimetypes import init
from msilib.schema import Error
import pyodbc

def mktable(dic, header=None):
    # get max col width
    col_widths = list(map(max, zip(*(map(lambda x: len(str(x)), (k,*v))
                                     for k,v in dic.items()))))

    # default numeric header if missing
    if not header:
        header = range(1, len(col_widths)+1)
    
    header_widths = map(lambda x: len(str(x)), header)
    
    # correct column width if headers are longer
    col_widths = [max(c,h) for c,h in zip(col_widths, header_widths)]
    
    # create separator line
    line = '+%s+' % '+'.join('-'*(w+2) for w in col_widths)
    #line = '-' * (sum(col_widths)+(len(col_widths)-1)*3+4)
    
    # create formating string
    fmt_str = '| %s |' % ' | '.join(f'{{:<{i}}}' for i in col_widths)
    
    # header
    print(line)
    print(fmt_str.format(*header))
    print(line)
    
    # data
    for k, v in dic.items():
        print(fmt_str.format(k, *v))
    
    # footer
    print(line)

def get_connection():
    conn = pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',host='DESKTOP-B81IS42\SQLEXPRESS', database='QLSinhVien',
                      trusted_connection='yes',encrypt='no')
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        
def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "select * from Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()
        
        print("Danh sach cac lop: ")
        for row in records:
            print("*"*50)
            print("Ma lop: ", row[0])
            print("Ten lop: ", row[1])
            
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Da co loi xay ra khi thuc thi. Thong tin loi: ", error)
        
def get_all_class_with_format():
    # try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "select * from Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()
        
        select_sinhVien = "select * from SinhVien"
        cursor.execute(select_sinhVien)
        records_sv = cursor.fetchall()
        print("Danh sach tat ca sinh vien la: ")
        student_dict = []
        
        for row in records_sv:
            sv = SinhVien(row[0],row[1], row[2])
            student_dict.append(sv)

            close_connection(connection)
            
        mktable(student_dict, header=('Ma so', 'Ho ten', 'Ma lop'))
    # except(Exception, pyodbc.Error) as error:
    #     print("Da co loi xay ra khi thuc thi. Thong tin loi: ", error)
        
get_all_class_with_format()

class SinhVien:
    # biến của lớp , chúng cho tất cả đối tượng thuộc lớp
    
    # hàm khởi tạo, hàm tạo lập : khởi gán các thuộc tính của đối tượng
    def __init__(self, maSo: int, hoTen: str, maLop: int):
        self._maSo = maSo #thuộc tính private
        self._hoTen = hoTen #thuộc tính private
        self._maLop = maLop #thuộc tính private
        
    #cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSo
    @property
    def maSo(self):
        return self._maSo
    
    # cho phép thay đổi giá trị của thuộc tính maSo
    @maSo.setter
    def maSo(self, maso):
        if self.laMsHopLe(maso):
            self._maSo = maso
            
    @property
    def hoTen(self):
        return self._hoTen
    
    @hoTen.setter
    def hoTen(self, hoten):
        self._hoTen = hoten
        
    @property
    def maLop(self):
        return self._maLop
    
    @maLop.setter
    def maLop(self, malop):
        self._maLop = malop
    # phương thức tĩnh : các phương thức không truy xuất gì đến thuộc tính , hành vi của lớp
    # những phương thức này không cần truyền tham số mặc định self
    # đây không phải là một hành vi ( phương thức ) của 1 đối tượng thuộc lớp
    @staticmethod
    def laMsHopLe(self, maso: int):
        return len(str(maso)) == 7
    # phương thức của lớp , chỉ truy xuất tới các biến thành viên của lớp
    # không truy xuất được các thuộc tính riêng của đối tượng
    
    #tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._maLop}"

    # hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self._maSo}\t{self._hoTen}\t{self._maLop}")
        
class DanhSachSv:
    def __init__(self):
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)