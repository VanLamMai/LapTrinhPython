# Python program to demonstrate
# accessing a element from a dictionary

# Creating a Dictionary
Dict = {1: 'Geeks', 'name' : 'For', 3: 'Geeks'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])

# Creating a Dictionary
Dict = {1: 'Geeks', 'name' : 'For', 3: 'Geeks'}

# accessing a element using get()
print("Accessing a element using get: ")
print(Dict.get(3))

# Creating a Dictionary
Dict = {'Dict1' : {1: 'Geeks'},
        'Dict2' : {'Name' : 'For'}}

# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'] [1])
print(Dict['Dict2'] ['Name'])