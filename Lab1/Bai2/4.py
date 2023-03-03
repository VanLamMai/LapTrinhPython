import math

n = int(input("Hãy nhập giá trị nguyên để kiểm tra Fibonacci: "))

def check_pefect_square(m):
    n = int (math.sqrt (m))
    return n * n == m

def check_Fibo(m):
    return check_pefect_square(5 * m * m - 4)

if(check_Fibo (n) == True):
    print(n, "là Fibonacci")
else:
    print(n, "Không là Fibonacci")