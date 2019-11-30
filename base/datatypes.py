#! /usr/bin/python


def main():
	# List
	my_list = [10, 20, 30, 40, 50]
	print("List", my_list)

	# Tuple
	my_tup = (1, 2, 3, 4, 5, 6)
	print("Tuple", my_tup)

	# Dict
	my_dict = {'name': 'Bronx', 'age': '2', 'occupation': "Corey's Dog"}
	print("Dict", my_dict)
	for key, val in my_dict.items():
		print("My {} is {}".format(key, val))

	# Set
	my_set = {10, 20, 30, 40, 50, 20, 30, 30, 40, 20}
	print("Set", my_set)


if __name__ == '__main__':
	main()
