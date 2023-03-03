from math import sqrt

def pTrinhBac2(a, b, c):
    x1 = 0
    x2 = 0
    delta = b ** 2 - 4 * a * c
    if delta < 0 :
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        print(f"Phuong trinh co nghiem kep x1 = x2 = {-(b / (2 * a))}")
    else:
        x1 = (-(b) + sqrt(delta)) / (2 * a)
        x2 = (-(b) - sqrt(delta)) / (2 * a)
        print(f"Phuong trinh co 2 nghiem phan biet x1 = {x1}, x2 = {x2}")

a = float(input("Nhap a = "))
b = float(input("Nhap b = "))
while True:
    if a == 0 and b == 0:
        print("Mot trong hai he so a va b phai khac 0")
        a = float(input("Nhap lai a = "))
        b = float(input("Nhap lai b = "))
    else:
        break

c = float(input("Nhap c = "))

pTrinhBac2(a, b, c)