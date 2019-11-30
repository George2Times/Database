from functools import reduce
import unittest


my_max = lambda x,y: x if x > y else y
my_square = lambda x: x**2
is_bigger_than_2 = lambda x: x > 2
mult_x_y = lambda x,y: x*y


# apply function to all items in list n
def to_all_in_list(input_list):
	return list(map(my_square, input_list))


# to iterate on list choosing elements
def filter_list(input_list):
	return list(filter(is_bigger_than_2, input_list))


# list to variable (1*2=2, 2*3=6, 6*4=24)
def list_to_var(input_list):
	return reduce(mult_x_y, input_list)


class TestSum(unittest.TestCase):
	n = [1,2,3,4]
	n2 = [1,4,9,16]
	n3 = [3,4]
	var = 24

	def test_my_max(self):
		self.assertEqual(my_max(1, 2), 2, "Should be 2")

	def test_to_all_in_list(self):
		self.assertEqual(to_all_in_list(self.n), self.n2, "Should be {}".format(self.n2))

	def test_filter_list(self):
		self.assertEqual(filter_list(self.n), self.n3, "Should be {}".format(self.n3))

	def test_list_to_var(self):
		self.assertEqual(list_to_var(self.n), self.var, "Should be {}".format(self.var))


if __name__ == '__main__':
	unittest.main()
