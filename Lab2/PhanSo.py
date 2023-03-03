from re import U
from unittest import result

class PhanSo:
    def __init__(self):
        self._tu = 0
        self._mau = 1

    @property
    def tu(self):
        return self._tu
    
    @tu.setter
    def tu(self, tu):
        self._tu = tu

    @property
    def mau(self):
        return self._mau

    @mau.setter
    def mau(self, mau):
        if(mau != 0):
            self._mau = mau
        else:
            print("Mau so khong hop le")

    def xuat(self):
        print(f"{str(self.tu)}\{str(self.mau)}")

    def __str__(self) -> str:
        return f"{self._tu}\{self._mau}"

    def rutGon(self):
        if self.tu % self.mau == 0:
            self.tu / self.mau
        if self.tu > self.mau:
            for i in range(2, self.mau + 1):
                if(self.tu % i == 0 and self.mau % i == 0):
                    self.tu = int(self.tu/i)
                    self.mau = int(self.mau/i)
        else:
            for i in range(2, self.tu + 1):
                if(self.tu % i == 0 and self.mau % i == 0):
                    self.tu = int(self.tu/i)
                    self.mau = int(self.mau/i)
        return self.xuat()

    def _add_(self, other):
        result = PhanSo()
        if self.mau == other.mau:
            result.tu = int(self.tu) + int(other.tu)
            result.mau = int(self.mau)
        else:
            result.mau = int(self.mau) * int(other.mau)
            result.tu = int(self.tu) * int(other.mau) + int(self.mau) * int(other.tu)
        return result
    
    def _multiadd_(self, other):
        if self.mau == other.mau:
            self.tu = int(self.tu) + int(other.tu)
            self.mau = int(self.mau)
            self.rutGon()
        else:
            self.mau = int(self.mau) * int(other.mau)
            self.tu = int(self.tu) * int(other.mau) + int(self.mau) * int(other.tu)
            self.rutGon()
        return self

    def _sub_(self, other):
        result = PhanSo()
        if self.mau == other.mau:
            if self.tu >= other.tu:
                result.tu = self.tu - other.tu
                result.mau = self.mau
            else:
                print('So bi tru phai lon hon so tru')
        else:
            if self.tu * other.mau >= self.mau * other.tu:
                result.mau = self.mau * other.mau
                result.tu = self.tu * other.mau - self.mau * other.tu
            else:
                print('So bi tru phai lon hon so tru')
        return result.xuat()

    def _mul_(self, other):
        result = PhanSo()
        result.tu = self.tu * other.tu
        result.mau = self.mau * other.mau
        return result.xuat()

    def _truediv_(self, other):
        result = PhanSo()
        result.tu = self.tu * other.mau
        result.mau = self.mau * other.tu
        return result.xuat()

# a = PhanSo()
# a.tu = 8
# a.mau = 4

# b = PhanSo()
# b.tu = 5
# b.mau = 3

# a.rutGon()
# a.__add__(b)
# a.__sub__(b)
# a.__mul__(b)
# a.__truediv__(b)