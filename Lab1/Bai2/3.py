from numpy import intp
from urllib3 import Retry


def isPrimeNum(a,b):
    if(a < 2 or b < 2):
        return False
    for n in range(a, b + 1):
        if b % n == 0:
            print(n)
a = int(input("Nhap so nguyen duong a = "))
b = int(input("Nhap so nguyen duong b = "))

isPrimeNum(a,b)