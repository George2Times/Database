#! /usr/bin/python

# List
print("List")
my_list = [10, 20, 30, 40, 50]
for i in my_list:
	print(i)

# Tuple
print("Tuple")
my_tup = (1, 2, 3, 4, 5, 6)
for i in my_tup:
	print(i)

# Dict
print("Dict")
my_dict = {'name': 'Bronx', 'age': '2', 'occupation': "Corey's Dog"}
for key,val in my_dict.items():
	print("My {} is {}".format(key,val))

# Set
print("Set")
my_set = {10, 20, 30, 40, 50, 20, 30, 30, 40, 20}
for i in my_set:
	print(i)

