import math
from os import system

list = [2,5,9,20,10,11,13,10,14,5,8,9,9]

def check_perfect_square (m):
    n = int (math.sqrt (m)) 
    return n * n == m 

def check_fibo (m ): 
    return check_perfect_square (5 * m * m + 4) or check_perfect_square (5 * m * m - 4) 

def isOdd(i):
    return i and 1

def XuatSoLeKhongChiaHetCho5(list):
    sb=""
    for i in list:
        if i%5!=0:
            sb = sb + str(i) + ", "
    print(sb) 
            
def XuatTatCaFibonacci(list):
    sb = ""
    for i in list:
        if check_fibo(i) == True:
            sb = sb + str(i) + ","
    print(sb)
    
def TimSoNguyenToLonNhat(list):
    result = []
    for i in list:
        if i<2:
            return False
        if i%len(list)==0:
            result.append(i)
    print(max(result))
    
def TimSoFibonacciMin(list):
    result = []
    for i in list:
        if check_fibo(i) == True:
            result.append(i)
    print(min(result))
    
def TrungBinhSoLe(list):
    result = []
    sum = 0
    for i in list:
        if isOdd(i) == 1:
            result.append(i)
    for i in result:
        sum+=i
    print(sum/len(result))
    
def TichSoLe(list):
    mul = 1
    for i in list:
        if (isOdd(i) == 1) and (i%3!=0):
            mul *=i
    print(mul)
            
def Swap(list, x, y):
    list[x], list[y] = list[y],list[x]
    print(list)
    
def Rev(list):
    print(list[::-1])
    
def maxSecond(list):
    maxst = max(list[0], list[1])
    maxnd = max(list[0], list[1])
    
    for i in range(2, len(list)):
        if list[i] > maxst:
            maxnd = maxst
            maxst = list[i]
        elif (list[i]>maxnd) and (maxst != list[i]):
            maxnd=list[i]
            
    print(maxnd)
        
def totalDigitsOfNumber(n):
    total = 0
    while (n>0):
        total = total + n%10
        n = int(n/10)
    return total

def sumDigitsOfNumber(list):
    sum = 0
    for i in list:
        sum+= totalDigitsOfNumber(i)
        
    print(sum)

def countElement(list, n):
    if(n in list):
        print(list.count(n))
    else:
        print('Khong ton tai phan tu trong mang!')
    
def printAppearNElement(list, n):
    result = []
    for i in list:
        if list.count(i) == n:
            result.append(i)
    print(result)
    
def maxCountElement(list):
    b = []
    c = []
    for i in range(len(list)-1):
        b.append(list.count(list[i]))
        
    for i in range(len(b)-1):
        if b[i]== max(b):
            c.append(list[i])
            
    print(c[0])
    
while True:
    print('Chọn chức năng muốn thực hiện: ')
    print('Nhập 1: Xuât tất cả các số lẻ không chia hết cho 5')
    print('Nhập 2: Xuất tất cả các số Fibonacci')
    print('Nhập 3: Tìm số nguyên tố lớn nhất')
    print('Nhập 4: Tìm số Fibonacci bé nhất')
    print('Nhập 5: Tính trung bình các số lẻ')
    print('Nhập 6: Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng')
    print('Nhập 7: Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ')
    print('Nhập 8: Đảo ngược trật tự các phần tử của danh sách')
    print('Nhập 9: Xuất tất cả các số lớn thứ nhì của danh sách')
    print('Nhập 10: Tính tổng các chữ số của tất cả các số trong danh sách')
    print('Nhập 11: Đếm số lần xuất hiện của một số trong danh sách')
    print('Nhập 12: Xuất các số xuất hiện n lần trong danh sách')
    print('Nhập 13: Xuất các số xuất hiện nhiều lần nhất trong danh sách')
    print('Nhập 0: Thoát chương trình')
    try:
        action = int(input())
        if action == 0:
            break
        elif type(action) != int:
            print('XIN MỜI NHẬP LẠI')
            action = int(input())
            system("CLS")
            print('Chọn chức năng muốn thực hiện: ')
            print('Nhập 1: Xuât tất cả các số lẻ không chia hết cho 5')
            print('Nhập 2: Xuất tất cả các số Fibonacci')
            print('Nhập 3: Tìm số nguyên tố lớn nhất')
            print('Nhập 4: Tìm số Fibonacci bé nhất')
            print('Nhập 5: Tính trung bình các số lẻ')
            print('Nhập 6: Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng')
            print('Nhập 7: Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ')
            print('Nhập 8: Đảo ngược trật tự các phần tử của danh sách')
            print('Nhập 9: Xuất tất cả các số lớn thứ nhì của danh sách')
            print('Nhập 10: Tính tổng các chữ số của tất cả các số trong danh sách')
            print('Nhập 11: Đếm số lần xuất hiện của một số trong danh sách')
            print('Nhập 12: Xuất các số xuất hiện n lần trong danh sách')
            print('Nhập 13: Xuất các số xuất hiện nhiều lần nhất trong danh sách')
            print('Nhập 0: Thoát chương trình')
    except:
        print('CHÚNG TÔI HIỆN CHƯA PHÁT TRIỂN TÍNH NĂNG ĐÓ, XIN MỜI NHẬP LẠI')
        action = 0

    match action:
        case 1:
            system("CLS")
            print('===========================')
            print("Xuât tất cả các số lẻ không chia hết cho 5")
            print('===========================')
            XuatSoLeKhongChiaHetCho5(list)
            print('===========================')
        case 2:
            system("CLS")
            print('===========================')
            print("Xuất tất cả các số Fibonacci")
            print('===========================')
            XuatTatCaFibonacci(list)
            print('===========================')
        case 3:
            system("CLS")
            print('===========================')
            print("Tìm số nguyên tố lớn nhất")
            print('===========================')
            TimSoNguyenToLonNhat(list)
            print('===========================')
        case 4:
            system("CLS")
            print('===========================')
            print("Tìm số Fibonacci bé nhất")
            print('===========================')
            TimSoFibonacciMin(list)
            print('===========================')
        case 5:
            system("CLS")
            print('===========================')
            print("Tính trung bình các số lẻ")
            print('===========================')
            TrungBinhSoLe(list)
            print('===========================')
        case 6:
            system("CLS")
            print('===========================')
            print("Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng")
            print('===========================')
            TichSoLe(list)
            print('===========================')
        case 7:
            system("CLS")
            print('===========================')
            print("Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ")
            print('===========================')
            Swap(list,1,4)
            print('===========================')
        case 8:
            system("CLS")
            print('===========================')
            print("Đảo ngược trật tự các phần tử của danh sách")
            print('===========================')
            Rev(list)
            print('===========================')
        case 9:
            system("CLS")
            print('===========================')
            print("Xuất tất cả các số lớn thứ nhì của danh sách")
            print('===========================')
            maxSecond(list)
            print('===========================')
        case 10:
            system("CLS")
            print('===========================')
            print("Tính tổng các chữ số của tất cả các số trong danh sách")
            print('===========================')
            sumDigitsOfNumber(list)
            print('===========================')
        case 11:
            system("CLS")
            print('===========================')
            print("Đếm số lần xuất hiện của một số trong danh sách")
            print('===========================')
            countElement(list, 9)
            print('===========================')
        case 12:
            system("CLS")
            print('===========================')
            print("Xuất các số xuất hiện n lần trong danh sách")
            print('===========================')
            printAppearNElement(list,2)
            print('===========================')
        case 13:
            system("CLS")
            print('===========================')
            print("Xuất các số xuất hiện nhiều lần nhất trong danh sách")
            print('===========================')
            maxCountElement(list)
            print('===========================')