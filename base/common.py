#! /usr/bin/python


# Fizz Buzz
for num in range(1, 21):
	if num % 5 == 0 and num % 3 == 0:
		print("FizzBuzz")
	elif num % 3 == 0:
		print("Fizz")
	elif num % 5 == 0:
		print("Buzz")
	else:
		print(num)

"""
# Fibonacci Seq
a, b = 0, 1
for i in range(1, 11):
	a, b = b, a+b
	print(i , ":" , a)
"""
