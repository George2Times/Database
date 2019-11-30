#! /usr/bin/python


def main():
	for item in fib(10):
		print(item)


# Fibonacci Generator
def fib(num):
	a, b = 0, 1
	for i in range(0, num):
		yield "{}: {}".format(i+1, a)
		a, b = b, a + b


if __name__ == '__main__':
	main()
