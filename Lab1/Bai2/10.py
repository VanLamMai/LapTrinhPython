def printTriangle(n):
    listStar = []
    for i in range(1, n + 1):
        listStar.append("*\t" * i)
    print("\n".join(listStar))

n = int(input("Nhap so hang : "))
printTriangle(n)