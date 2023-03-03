def Fibonacci_with_recursive(n):
    if(n < 0):
        return - 1
    elif(n == 0 or n == 1):
        return n
    else:
        return Fibonacci_with_recursive(n - 1) + Fibonacci_with_recursive(n - 2)

list_Fibonacci = []

n = int(input("Nhập số nguyên dương n : "))
for i in range(0, n + 1):
    list_Fibonacci.append(Fibonacci_with_recursive(i))

print(f"Tổng của dãy {n} số Fibonacci là {sum(list_Fibonacci)}")