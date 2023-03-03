#Accessing Tuple
#with Indexing
from typing import Tuple


Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[0])

#Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")

#This line unpack
#values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)