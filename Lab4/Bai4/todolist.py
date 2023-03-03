from tkinter import *

from tkinter import messagebox

tasks_list = []

counter = 1

def inputError() :
	if enterTaskField.get() == "" :
		messagebox.showerror("Input Error")
		return 0
	return 1

def clear_taskNumberField() :
	taskNumberField.delete(0.0, END)

def clear_taskField() :
	enterTaskField.delete(0, END)
	
def insertTask():
	global counter
	value = inputError()

	if value == 0 :
		return
	content = enterTaskField.get() + "\n"
	tasks_list.append(content)
	TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
	counter += 1
	clear_taskField()

def delete() :
	global counter

	if len(tasks_list) == 0 :
		messagebox.showerror("No task")
		return
	number = taskNumberField.get(1.0, END)
	if number == "\n" :
		messagebox.showerror("input error")
		return
	
	else :
		task_no = int(number)

	clear_taskNumberField()
	tasks_list.pop(task_no - 1)
	counter -= 1
	TextArea.delete(1.0, END)

	for i in range(len(tasks_list)) :
		TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
	
if __name__ == "__main__" :

	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background = "light green")

	# set the title of GUI window
	gui.title("ToDo App")

	# set the configuration of GUI window
	gui.geometry("250x300")

	# create a label : Enter Your Task
	enterTask = Label(gui, text = "Enter Your Task", bg = "light green")

	# create a text entry box
	# for typing the task
	enterTaskField = Entry(gui)

	# create a Submit Button and place into the root window
	# when user press the button, the command or
	# function affiliated to that button is executed
	Submit = Button(gui, text = "Submit", fg = "Black", bg = "Red", command = insertTask)

	# create a text area for the root
	# with lunida 13 font
	# text area is for writing the content
	TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")

	# create a label : Delete Task Number
	taskNumber = Label(gui, text = "Delete Task Number", bg = "blue")
						
	taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")

	# create a Delete Button and place into the root window
	# when user press the button, the command or
	# function affiliated to that button is executed .
	delete = Button(gui, text = "Delete", fg = "Black", bg = "Red", command = delete)

	# create a Exit Button and place into the root window
	# when user press the button, the command or
	# function affiliated to that button is executed .
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
	enterTask.grid(row = 0, column = 2)

	# ipadx attributed set the entry box horizontal size			
	enterTaskField.grid(row = 1, column = 2, ipadx = 50)
						
	Submit.grid(row = 2, column = 2)
		
	# padx attributed provide x-axis margin
	# from the root window to the widget.
	TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
						
	taskNumber.grid(row = 4, column = 2, pady = 5)
						
	taskNumberField.grid(row = 5, column = 2)

	# pady attributed provide y-axis
	# margin from the widget.				
	delete.grid(row = 6, column = 2, pady = 5)
						
	Exit.grid(row = 7, column = 2)

	# start the GUI
	gui.mainloop()