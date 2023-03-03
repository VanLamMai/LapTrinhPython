def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)

n = int(input("Nhap so nguyen duong n = "))
print(giaiThua(n))