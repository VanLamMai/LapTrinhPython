from audioop import add
from numpy import place


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")

print ("Hello  " + lname + " " + fname)
print(f"Hello {lname} {fname}")
print("Hello {} {}".format(lname, fname))