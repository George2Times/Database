#! /usr/bin/python


def main():
	my_list = [i for i in range(1,11)]
	print(my_list)

	# Give me each number in a list squared
	squares = [num*num for num in my_list]
	print(squares)


if __name__ == '__main__':
	main()
