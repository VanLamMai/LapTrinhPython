"Dùng đệ quy"
def Fibonacci_with_recursive(n):
    if(n < 0):
        return -1
    elif(n == 0 or n == 1):
        return n
    else:
        return Fibonacci_with_recursive(n - 1) + Fibonacci_with_recursive(n - 2)

n = int(input("Nhap so nguyen duong n = "))
print(f"Số Fibonacci thứ {n} dùng đệ quy là: {str(Fibonacci_with_recursive(n))}")

"Không dùng đệ quy"
def Fibonacci_without_recursive(n):
    a = 0,
    b = 1,
    c = 1

    if(n < 0):
        return - 1
    else:
        for i in range(2, n):
            a = b
            b = c
            c = a + b
        return c

n = int(input("Nhap so nguyen duong n = "))
print(f"Số Fibonacci không dùng đệ quy là: {str(Fibonacci_without_recursive(n))}")