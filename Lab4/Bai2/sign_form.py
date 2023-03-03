import tkinter as tk

root = tk.Tk()

root.geometry("600x400")

name_var = tk.StringVar()
password_var = tk.StringVar()

def submit():
    name = name_var.get()
    password = password_var.get()

    print("The name is : " +name)
    print("The password is : " + password)

    name_var.set("")
    password_var.set("")

name_lb = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre',10,'normal'))
password_lb = tk.Label(root, text='Password', font=('calibre',10, 'bold'))
password_entry = tk.Entry(root, textvariable=password_var, font=('calibre', 10, 'normal'), show='*')

submit_btn = tk.Button(root, text='Submit', command=submit)

name_lb.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
password_lb.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
submit_btn.grid(row=2, column=1)

root.mainloop()