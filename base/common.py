#! /usr/bin/python


def main():
	fizz_buzz(5)
	fibonacci_seq(5)


# Fizz Buzz
def fizz_buzz(n):
	print("Fizz Buzz for {}".format(n))
	for num in range(1, n):
		if num % 5 == 0 and num % 3 == 0:
			print("FizzBuzz")
		elif num % 3 == 0:
			print("Fizz")
		elif num % 5 == 0:
			print("Buzz")
		else:
			print(num)
	return


# Fibonacci Seq
def fibonacci_seq(n):
	print("Fibonacci sequence for {}".format(n))
	a, b = 0, 1
	for i in range(1, n):
		a, b = b, a+b
		print(i , ":" , a)


if __name__ == '__main__':
	main()
