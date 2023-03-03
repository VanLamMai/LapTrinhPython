from cmath import isnan
import re
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

def onVaslid(id,name,dob,email,phone, course, year, sub):
    if (checkEmail(email.get()) or checkDate(dob.get()) or len(str(id.get())) < 7 or id == 0 
    or len(str(name.get())) == 0 or len(str(phone.get())) < 10 
    or len(str(course.get())) == 0 or len(str(year.get())) == 0 or len(sub) == 0):
        messagebox.showerror('Lỗi', 'Bạn chưa nhập đúng, đủ thông tin! vui lòng nhập lại')
        return False
    print(str(id.get()) + name.get() + email.get() + phone.get() + str(course.get()) + year.get() + str(len(sub)))
    return True

def checkEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, str(email))

def focus1(event):
    year_field.focus_set()

def checkDate(date):
    regex = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
    return re.match(regex, str(date))
    
def submit(id, name, email,dob, phone, course, year, sub):
    onVaslid(id, name, dob, email,phone, course, year, sub)

if __name__ =="__main__":
    root = Tk()

    root.configure(background='light green')
    root.title('ĐĂNG KÝ HỌC PHẦN')
    root.geometry('800x500')
    
    picks = ['Pyhton', 'Java', 'CNPM', 'Web']
    
    def only_numbers(char):
        return char.isdigit()
    
    validation_id = root.register(only_numbers)
    
    id = IntVar(value=0000000)
    name = StringVar()
    dob = StringVar()
    email = StringVar()
    phone = StringVar()
    course = IntVar(value=1)
    year = StringVar()
    sub = []
    
    title = Label(root, text='THÔNG TIN ĐĂNG KÝ HỌC PHẦN', fg='Red', bg='light green', font=("Arial", 20))
    
    id_lb = Label(root, text='Mã số sinh viên', bg='light green')
    name_lb = Label(root, text='Họ tên', bg='light green')
    dob_lb = Label(root, text='Ngày sinh', bg='light green')
    email_lb = Label(root, text='Email', bg='light green')
    phone_lb = Label(root, text='Số điện thoại', bg='light green')
    course_lb = Label(root, text='Học kỳ', bg='light green')
    year_lb = Label(root, text='Năm học', bg='light green')
    sub_lb = Label(root, text='Môn học', bg='light green')
    
    id_field = Entry(root,width=60, font=('Arial 11'), textvariable=id, validate='key', validatecommand=(validation_id, '%s'))
    name_field = Entry(root,width=60, font=('Arial 11'), textvariable=name)
    dob_field = Entry(root,width=60, font=('Arial 11'), textvariable=dob)
    email_field = Entry(root,width=60, font=('Arial 11'), textvariable=email)
    phone_field = Entry(root,width=60, font=('Arial 11'), textvariable=phone)
    course_field = Entry(root,width=60, font=('Arial 11'), textvariable=course)
    year_field = Combobox(root,width=58, font=('Arial 11'), textvariable=year)
    year_field['values'] = ('2022-2023', '2023-2024', '2024-2025')
    year_field['state'] = 'readonly'
    year_field.bind('<<ComboboxSelected>>', focus1)
    
    submit_btn = Button(root,text='Đăng Ký', command=lambda : submit(id, name, dob,email,phone,course,year, sub))
    exit_btn = Button(root, text='Thoát', command=root.destroy)
    
    for pick in picks:
        var = StringVar()
        chk = Checkbutton(root, text=pick, variable=var)
        chk.pack(side=LEFT, anchor='e', expand=YES)
        sub.append(var.get())
    
    title.place(relx=0.5, rely=0.1,anchor=CENTER)
    id_lb.place(relx=0.1,rely=0.15)
    name_lb.place(relx=0.1,rely=0.2)
    dob_lb.place(relx=0.1,rely=0.25)
    email_lb.place(relx=0.1,rely=0.3)
    phone_lb.place(relx=0.1,rely=0.35)
    course_lb.place(relx=0.1,rely=0.4)
    year_lb.place(relx=0.1,rely=0.45)
    sub_lb.place(relx=0.1,rely=0.5)
    
    id_field.place(relx=0.25,rely=0.15)
    name_field.place(relx=0.25,rely=0.2)
    dob_field.place(relx=0.25,rely=0.25)
    email_field.place(relx=0.25,rely=0.3)
    phone_field.place(relx=0.25,rely=0.35)
    course_field.place(relx=0.25,rely=0.4)
    year_field.place(relx=0.25,rely=0.45)
    
    submit_btn.place(relx=0.5, rely=0.8)
    exit_btn.place(relx=0.6, rely=0.8)

    root.mainloop()