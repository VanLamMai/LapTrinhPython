#1 Tìm và sửa lỗi
# if 5 > 2:
#     print("Năm lớn hơn hai!")
    
#2 Bỏ kí tự hợp lệ ở tên biến sau
# myfirst_name = "John"

#3 Thêm từ khoá để biến x thành biến toàn cục
# def myfunc():
#     global x
#     x = "fantastic"
    
#4 Cho biết kết quả của chương trình sau
# x = "Hello World"
# print(type(x)) #str

#5 Cho biết kết quả của chương trình sau 
# x = ("apple", "banana", "cherry")
# print(type(x)) # tuple

#6 Điền vào từ khoá để chuyển x sang kiểu số thực
# x = 5
# x = float(x)

#7 Trả về chuỗi không có khoảng trắng ở đầu và cuối
# txt = " Hello World "
# x = txt.strip()

#8 Thay thế ký tự H thành J
# txt = "Hello World"
# txt = txt.replace('H', 'J')

#9 Điền phần còn thiếu vào chỗ trống
# age = 36
# txt = "My name is John, and I am {0}"
# print(txt.format(age))

#10 Cho biết kết quả của dòng lệnh
# print(bool("abc")) #True

#11 Cho biết kết quả của dòng lệnh
# print(10 == 9) #False

#12 Điền từ khoá thích hợp để câu lệnh bên trong if được xuất ra màn hình
# if 5==10 or 4==4:
#     print("Một trong hai điều kiện đúng")
    
#13 Cho biết kết quả của dòng lệnh
# print(10//4) #2

#14 Cho biết kết quả xuất ra của dòng lệnh
# sum = 0
# for i in range(1,10,2):
#     sum+=i
# print(sum) #25c

#15 Cho biết kết quả xuất ra của dòng lệnh
# i=0
# while i<5:
#     print(i)
#     i+=1

#16 Cho biết kết quả xuất ra của dòng lệnh
# sum = 0
# for i in range(5):
#     sum+=i
#     print(sum)

#17 Thay đổi apple thành kiwi của list sau:
# fruits = ["apple", "banana", "cherry"]
# fruits[0] = "kiwi"

#18 Thêm lemon vào vị trí thứ 2 của danh sách
# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "lemon"

#19 LấY giá trị pần tử cuối cùng bằng chỉ số âm
# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])

#20 Cho biết kết quả của dòng lệnh
# x = lambda a : a + 10
# print(x(5)) #15

#21 Xuất phần tử thứ 3,4,5 của danh sách
# fruits = ["apple", "banana", "cherry", "orange", "kiwi",
# "melon", "mango"]
# print(fruits[3:6])

#22 Cho kết quả của dòng lệnh
# fruits = ["apple", "banana", "cherry", "orange", "kiwi",
# "melon", "mango"]
# print(fruits[4:]) # pos 4 to last

#23 Cho dòng lệnh, viết thêm câu lệnh để thêm 'lemon' vào cuối
# fruits = {"apple", "banana", "cherry"}
# fruits.add('lemon')

#24 Cho dòng lệnh, sử dụng lệnh "discard" để xoá "banana" khỏi mảng
# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")

#25 Viết lệnh thêm cặp "color":"red" vào cuối của car
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# car['color'] = 'red'

#26 Thay đổi năm từ 1964 ->2020
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# car['year'] = 2020


#27 Điền vào chỗ trống để khi i=3 sẽ nhảy tới vòng lặp tiếp theo
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

#28 Điền tham số thích hợp vào chỗ trống
# def my_function(kids):
#     print("The youngest child is " + kids[2])

#29 Hãy tạo ra một đối tượng của lớpMyClass có tên p1
# class MyClass:
#     x=5
# p1 = MyClass()

#30 Điền từ thích hợp vào chỗ trống
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#31 CHo biết kết quả của dòng lệnh
# def myfunc(n):
#     return lambda a : a * n

# mydoubler = myfunc(2)
# print(mydoubler(11)) #22

#32 
# list1 = [3, 4, 5, 20, 5, 25, 1, 3]
# list1.pop(1) #xoá vị trí số 2

#33

# from time import time


# print(time())

#34 Hàm được định nghĩa bên trong lớp được gọi là function
#35 Toán tử nào là quá tải hàm của hàm or() -> a
#36 Kết quả đầu ra của đoạn chương trình sau:
# i = 0
# while i < 3:
#     print(i)
#     i+=1
#     print(i+1)
#37 Kết quả
# print("Dalat university"[::-1]) # Đảo ngược chuỗi

#38 None
#39 Kết quả xuất ra của chương tình:
# print (0.1 + 0.2==0.3) #False

#40 5 trừ nhị phân
#41 -19
#42 D
#43 C
#44 D
#45 
# L = [1, 23, 'hello', 1]
#list

#46 6
#47 
D = dict()
for x in enumerate(range(2)):
    D[x[0]] = x[1]
    D[x[1]+7] = x[0]
print(D)