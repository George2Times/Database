#! /usr/bin/python


def main():
	corney = Person('Corney')
	corney.reveal_identity()

	wade = SuperHero('Wade Wilson', 'Deadpool')
	wade.reveal_identity()


class Person(object):
	def __init__(self, name):
		self.name = name

	def reveal_identity(self):
		print("My name is {}".format(self.name))


class SuperHero(Person):
	def __init__(self, name, hero_name):
		super(SuperHero, self).__init__(name)
		self.hero_name = hero_name

	def reveal_identity(self):
		super(SuperHero, self).reveal_identity()
		print("...And I am {}".format(self.hero_name))


if __name__ == '__main__':
	main()
