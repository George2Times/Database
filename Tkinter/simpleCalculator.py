from tkinter import *
import math


class SimpleCalculator:

	def __init__(self, master):
		self.master = master
		master.title("Simple Calculator")
		master.configure(background='blue')
		master.minsize(200, 150)
		master.maxsize(500, 500)
		# root.geometry("1400x850")
		self.e = Entry(fg="white", bg="black", master=self.master, textvariable=1, width=20, borderwidth=2,
						justify='right', font=("Calibri", 30))
		self.first_number = 0
		self.second_number = 0
		self.math = "none"
		self.last_button_pressed = "none"

		self.gui_init()

	def gui_init(self):
		self.e.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=5, ipady=5)

		button_1 = Button(self.master, text="1", padx="40", pady="20", command=lambda: self.number_button_click(self, 1))
		button_2 = Button(self.master, text="2", padx="40", pady="20", command=lambda: self.number_button_click(self, 2))
		button_3 = Button(self.master, text="3", padx="40", pady="20", command=lambda: self.number_button_click(self, 3))
		button_4 = Button(self.master, text="4", padx="40", pady="20", command=lambda: self.number_button_click(self, 4))
		button_5 = Button(self.master, text="5", padx="40", pady="20", command=lambda: self.number_button_click(self, 5))
		button_6 = Button(self.master, text="6", padx="40", pady="20", command=lambda: self.number_button_click(self, 6))
		button_7 = Button(self.master, text="7", padx="40", pady="20", command=lambda: self.number_button_click(self, 7))
		button_8 = Button(self.master, text="8", padx="40", pady="20", command=lambda: self.number_button_click(self, 8))
		button_9 = Button(self.master, text="9", padx="40", pady="20", command=lambda: self.number_button_click(self, 9))
		button_0 = Button(self.master, text="0", padx="40", pady="20", command=lambda: self.number_button_click(self, 0))
		button_add = Button(self.master, text="+", padx="40", pady="20", command=lambda: self.button_function(self, "addition"))
		button_equal = Button(self.master, text="=", padx="40", pady="20", command=self.button_equal)

		button_x = Button(self.master, text="x", padx="40", pady="20", command=lambda: self.button_function(self, "multiplication"))
		button_sub = Button(self.master, text="-", padx="40", pady="20", command=lambda: self.button_function(self, "subtraction"))
		button_dot = Button(self.master, text=".", padx="40", pady="20", command=self.button_dot)
		button_sign = Button(self.master, text="+/-", padx="40", pady="20", command=self.button_sign)

		button_percent = Button(self.master, text="%", padx="40", pady="20", command=self.button_percent)
		button_sqrt = Button(self.master, text="sqrt", padx="40", pady="20", command=self.button_sqrt)
		button_pow = Button(self.master, text="pow", padx="40", pady="20", command=self.button_pow)
		button_hip = Button(self.master, text="1/x", padx="40", pady="20", command=self.button_hip)

		button_ce = Button(self.master, text="CE", padx="40", pady="20", command=self.button_ce)
		button_c = Button(self.master, text="C", padx="40", pady="20", command=self.button_c)
		button_correct = Button(self.master, text="Correct", padx="40", pady="20", command=self.correct)
		button_div = Button(self.master, text="/", padx="40", pady="20", command=lambda: self.button_function(self, "division"))

		button_percent.grid(row=1, column=0)
		button_sqrt.grid(row=1, column=1)
		button_pow.grid(row=1, column=2)
		button_hip.grid(row=1, column=3)

		button_ce.grid(row=2, column=0)
		button_c.grid(row=2, column=1)
		button_correct.grid(row=2, column=2)
		button_div.grid(row=2, column=3)

		button_7.grid(row=3, column=0)
		button_8.grid(row=3, column=1)
		button_9.grid(row=3, column=2)
		button_x.grid(row=3, column=3)

		button_4.grid(row=4, column=0)
		button_5.grid(row=4, column=1)
		button_6.grid(row=4, column=2)
		button_sub.grid(row=4, column=3)

		button_1.grid(row=5, column=0)
		button_2.grid(row=5, column=1)
		button_3.grid(row=5, column=2)
		button_add.grid(row=5, column=3)

		button_sign.grid(row=6, column=0)
		button_0.grid(row=6, column=1)
		button_dot.grid(row=6, column=2)
		button_equal.grid(row=6, column=3)

	def clear(self):
		self.e.delete(first=0, last="end")

	def correct(self):
		current = self.e.get()
		self.clear()
		self.e.insert(0, current[:-1])

	def number_button_click(self, master, number):
		current = self.e.get()
		self.clear()
		self.e.insert(0, current + str(number))

	def button_function(self, master, function_button_id):
		self.first_number = self.e.get()
		self.clear()
		self.math = function_button_id

	def button_percent(self):
		current = str(float(self.e.get()) / 100)
		self.clear()
		self.e.insert(0, current)

	def button_dot(self):
		current = self.e.get()
		if current.find(".") == -1:
			current = current + "."
			self.clear()
			self.e.insert(0, current)

	def button_sqrt(self):
		current = math.sqrt(float(self.e.get()))
		self.clear()
		if current - int(current) == 0.0:
			current = str(int(current))
		self.e.insert(0, current)

	def button_pow(self):
		current = float(self.e.get())**2
		self.clear()
		if current-int(current) == 0.0:
			current = str(int(current))
		self.e.insert(0, current)

	def button_hip(self):
		current = 1 / float(self.e.get())
		self.clear()
		if current - int(current) == 0.0:
			current = str(int(current))
		self.e.insert(0, current)

	def button_ce(self):
		self.clear()
		self.first_number = 0.0

	def button_c(self):
		self.button_ce()
		self.second_number = 0.0

	def button_sign(self):
		current = int(self.e.get())
		current = -current
		self.clear()
		self.e.insert(0, str(current))

	def button_equal(self):
		if self.last_button_pressed != "equal":
			self.second_number = self.e.get()
		else:
			self.first_number = self.e.get()
		self.e.delete(0, END)
		if self.math == "addition":
			result = float(self.first_number) + float(self.second_number)
		elif self.math == "subtraction":
			result = float(self.first_number) - float(self.second_number)
		elif self.math == "multiplication":
			result = float(self.first_number) * float(self.second_number)
		elif self.math == "division":
			result = float(self.first_number) / float(self.second_number)
		elif self.math == "multiplication":
			result = float(self.first_number) / float(self.second_number)
		else:
			self.e.insert(0, "error")
			return
		if result-int(result) == 0.0:
			result = int(result)
		self.button_ce()
		self.e.insert(0, result)
		self.last_button_pressed = "equal"


def main():
	root = Tk()
	app = SimpleCalculator(root)
	root.mainloop()


if __name__ == '__main__':
	main()
