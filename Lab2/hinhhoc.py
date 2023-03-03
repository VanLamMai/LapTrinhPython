class HinhHoc:
    def __init__(self, canh: float):
        self._canh = canh

    @property
    def canh(self):
        return self._canh

    @canh.setter
    def canh(self, canh: float):
        self._canh = canh

    def dienTich(self):
        pass

    def __str__(self) -> str:
        return f"Hinh Hoc"