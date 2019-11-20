#! /usr/bin/python

"""
# Fibonacci Seq
a, b = 0, 1
for i in range(1, 11):
	a, b = b, a+b
	print(i , ":" , a)
"""


# Fibonacci Generator
def fib(num):
	a, b = 0, 1
	for i in range(0, num):
		yield "{}: {}".format(i+1, a)
		a, b = b, a + b


for item in fib(10):
	print(item)
