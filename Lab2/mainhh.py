from os import system
from ds_hinh_hoc import DanhSachHH
from hinhvuong import HinhVuong


dshh = DanhSachHH()
while True:
    print('Chọn chức năng muốn thực hiện: ')
    print('Nhập 1: Thêm Hình')
    print('Nhập 2: Xuất Hình')
    print('Nhập 3: Tìm hình có diện tích lớn nhất')
    print('Nhập 4: Tìm hình có diện tích nhỏ nhất')
    print('Nhập 5: Tìm hình tròn nhỏ nhất')
    print('Nhập 6: Sắp các hình giảm dần theo diện tích')
    print('Nhập 7: Đếm số lượng hình theo loại')
    print('Nhập 8: Tính tổng diện tích các hình')
    print('Nhập 9: Tìm hình có diện tích lớn nhất theo loại hình học cho trước')
    print('Nhập 10: Tìm vị trí của hình H trong danh sách')
    print('Nhập 11: Tìm hình theo diện tích')
    print('Nhập 12: Xoá một hình học khỏi danh sách')
    print('Nhập 13: Xoá tất cả các hình theo loại cho trước')
    print('Nhập 14: Xuất danh sách hình theo loại cho trước và sắp tăng hoặc giảm')
    print('Nhập 15: Tính tổng diện tích các hinh theo loại')
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
            print('Nhập 1: Thêm Hình')
            print('Nhập 2: Xuất Hình')
            print('Nhập 3: Tìm hình có diện tích lớn nhất')
            print('Nhập 4: Tìm hình có diện tích nhỏ nhất')
            print('Nhập 5: Tìm hình tròn nhỏ nhất')
            print('Nhập 6: Sắp các hình giảm dần theo diện tích')
            print('Nhập 7: Đếm số lượng hình theo loại')
            print('Nhập 8: Tính tổng diện tích các hình')
            print('Nhập 9: Tìm hình có diện tích lớn nhất theo loại hình học cho trước')
            print('Nhập 10: Tìm vị trí của hình H trong danh sách')
            print('Nhập 11: Tìm hình theo diện tích')
            print('Nhập 12: Xoá một hình học khỏi danh sách')
            print('Nhập 13: Xoá tất cả các hình theo loại cho trước')
            print('Nhập 14: Xuất danh sách hình theo loại cho trước và sắp tăng hoặc giảm')
            print('Nhập 15: Tính tổng diện tích các hinh theo loại')
            print('Nhập 0: Thoát chương trình')
    except:
        print('CHÚNG TÔI HIỆN CHƯA PHÁT TRIỂN TÍNH NĂNG ĐÓ, XIN MỜI NHẬP LẠI')
        action = 0

    match action:
        case 1:
            system("CLS")
            print('===========================')
            print("Thêm Hình")
            print('===========================')
            dshh.readFile('hinhhoc.txt')
            print('===========================')
        case 2:
            system("CLS")
            print('===========================')
            print("Xuất hình")
            print('===========================')
            dshh.xuat()
            print('===========================')
        case 3:
            system("CLS")
            print('===========================')
            print("Tìm hình có diện tích lớn nhất")
            print('===========================')
            dshh.timHinhCoDienTichLonNhat()
            print('===========================')
        case 4:
            system("CLS")
            print('===========================')
            print("Tìm hình có diện tích nhỏ nhất")
            print('===========================')
            dshh.timHinhCoDienTichNhoNhat()
            print('===========================')
        case 5:
            system("CLS")
            print('===========================')
            print("Tìm hình tròn có diện tích lớn nhất")
            print('===========================')
            dshh.timHinhCoDienTichLonNhatTheoLoai('HinhTron')
            print('===========================')
        case 6:
            system("CLS")
            print('===========================')
            print("Sắp xếp danh sáchgiảm dần theo diện tích")
            print('===========================')
            dshh.sapXepTheoDienTich()
            dshh.xuat()
            print('===========================')
        case 7:
            system("CLS")
            print('===========================')
            print("Đếm số lượng hình theo loại")
            print('===========================')
            print(dshh.demSoLuongHinhTheoLoai("HinhTron"))
            print('===========================')
        case 8:
            system("CLS")
            print('===========================')
            print("Tính tổng diện tích các hình")
            print('===========================')
            print(dshh.tinhTongDienTich())
            print('===========================')
        case 9:
            system("CLS")
            print('===========================')
            print("Tìm hình có diện tích lớn nhất theoloại")
            print('===========================')
            dshh.timHinhCoDienTichLonNhatTheoLoai('HinhVuong')
            print('===========================')
        case 10:
            system("CLS")
            print('===========================')
            print("Tìm vị trí của hình")
            print('===========================')
            dshh.timViTriCuaHinh()
            print('===========================')
        case 11:
            system("CLS")
            print('===========================')
            print("Tìm hình theo diện tích")
            print('===========================')
            kq = dshh.timHinhTheoDienTich(25)
            print(*kq)
            print('===========================')
        case 12:
            system("CLS")
            print('===========================')
            print("Xoá một hình")
            print('===========================')
            hv = HinhVuong(5)
            dshh.xoa(hv)
            dshh.xoat()
            print('===========================')
        case 13:
            system("CLS")
            print('===========================')
            print("Xoá tất cả hình theo loại")
            print('===========================')
            
            print('===========================')
        case 14:
            system("CLS")
            print('===========================')
            print("Xuất danh sách hình theo loại và sắp xếp tăng hoặc giảm")
            print('===========================')
            
            print('===========================')
        case 15:
            system("CLS")
            print('===========================')
            print("Tính tổng diện tích các hình theo loại")
            print('===========================')
            
            print('===========================')