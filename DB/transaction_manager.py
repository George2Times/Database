import tkinter as tk
from tkinter import messagebox, StringVar, Label, Entry, Listbox, Scrollbar, Button

# from db import Database
from DB.db import Database


class Application(tk.Frame):
	"""
		GUI to make changes in db
	"""
	transaction_text: StringVar
	transaction_label: Label
	transaction_entry: Entry

	customer_text: StringVar
	customer_label: Label
	customer_entry: Entry

	retailer_text: StringVar
	retailer_label: Label
	retailer_entry: Entry

	price_text: StringVar
	price_label: Label
	price_entry: Entry

	transactions_list: Listbox
	scrollbar: Scrollbar

	add_btn: Button
	remove_btn: Button
	update_btn: Button
	clear_btn: Button

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		master.title('TRANSACTIONS Manager')
		# Width height
		master.geometry("700x350")
		# Create widgets/grid
		self.create_widgets()
		# Init selected item var
		self.selected_item = 0
		# Populate initial list
		self.populate_list()

	def create_widgets(self):
		# Transaction
		self.transaction_text = tk.StringVar()
		self.transaction_label = tk.Label(
			self.master, text='Transaction Name', font=('bold', 14), pady=20
		)
		self.transaction_label.grid(row=0, column=0, sticky=tk.W)
		self.transaction_entry = tk.Entry(
			self.master, textvariable=self.transaction_text
		)
		self.transaction_entry.grid(row=0, column=1)

		# Customer
		self.customer_text = tk.StringVar()
		self.customer_label = tk.Label(
			self.master, text='Customer', font=('bold', 14), pady=20
		)
		self.customer_label.grid(row=0, column=2, sticky=tk.W)
		self.customer_entry = tk.Entry(
			self.master, textvariable=self.customer_text
		)
		self.customer_entry.grid(row=0, column=3)

		# Retailer
		self.retailer_text = tk.StringVar()
		self.retailer_label = tk.Label(
			self.master, text='Retailer', font=('bold', 14), pady=20
		)
		self.retailer_label.grid(row=1, column=0, sticky=tk.W)
		self.retailer_entry = tk.Entry(
			self.master, textvariable=self.retailer_text
		)
		self.retailer_entry.grid(row=1, column=1)

		# Price
		self.price_text = tk.StringVar()
		self.price_label = tk.Label(
			self.master, text='Price',
			font=('bold', 14), pady=20		)
		self.price_label.grid(row=1, column=2, sticky=tk.W)
		self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
		self.price_entry.grid(row=1, column=3)

		# Buttons
		self.add_btn = tk.Button(
			master=self.master, text="Add transaction",
			command=self.add_item)
		self.add_btn.grid(row=2, column=0, pady=20)

		self.remove_btn = tk.Button(
			master=self.master, text="Remove transaction",
			command=self.remove_item)
		self.remove_btn.grid(row=2, column=1)

		self.update_btn = tk.Button(
			master=self.master, text="Update transaction",
			command=self.update_item)
		self.update_btn.grid(row=2, column=2)

		self.clear_btn = tk.Button(
			master=self.master, text="Clear Input",
			command=self.clear_text)
		self.clear_btn.grid(row=2, column=3)

		# Transactions list (listbox)
		self.transactions_list = tk.Listbox(
			self.master, height=8, width=50, border=1
		)
		self.transactions_list.grid(
			row=3, column=0, columnspan=3,
			rowspan=6, pady=20, padx=20)
		# Create scrollbar
		self.scrollbar = tk.Scrollbar(self.master)
		self.scrollbar.grid(row=3, column=3)
		# Set scrollbar to transactions listbox
		self.transactions_list.configure(yscrollcommand=self.scrollbar.set)
		self.scrollbar.configure(command=self.transactions_list.yview)
		# Bind select transaction from list
		self.transactions_list.bind('<<ListboxSelect>>', self.select_item)

	def populate_list(self):
		"""
			Delete items before update.
			so when you keep pressing it doesnt keep getting (show example by calling this twice)
		"""
		self.transactions_list.delete(0, tk.END)
		# Loop through records
		for row in db.fetch():
			# Insert into list
			self.transactions_list.insert(tk.END, row)

	# Clear all text fields
	def clear_text(self):
		self.transaction_entry.delete(0, tk.END)
		self.customer_entry.delete(0, tk.END)
		self.retailer_entry.delete(0, tk.END)
		self.price_entry.delete(0, tk.END)

	# Put data to entry when item selected in listbox
	def select_item(self, event):
		try:
			# Get item index
			index = self.transactions_list.curselection()[0]
			self.selected_item = self.transactions_list.get(index)
			# check if working
			# print(self.selected_item)

			# Add selected item data to entries
			self.clear_text()
			self.transaction_entry.insert(tk.END, self.selected_item[1])
			self.customer_entry.insert(tk.END, self.selected_item[2])
			self.retailer_entry.insert(tk.END, self.selected_item[3])
			self.price_entry.insert(tk.END, self.selected_item[4])
		except IndexError:
			pass

	def add_item(self):
		try:
			if self.transaction_text.get() == '':
				messagebox.showerror("Required Field", "Please add Transaction name")
				return
			if self.customer_text.get() == '':
				messagebox.showerror("Required Field", "Please add Customer")
				return
			if self.retailer_text.get() == '':
				messagebox.showerror("Required Field", "Please add Retailer")
				return
			if self.price_text.get() == '':
				messagebox.showerror("Required Field", "Please add Price")
				return

			print(self.transaction_text.get())
			# insert to db
			db.insert(self.transaction_text.get(), self.customer_text.get(),
			          self.retailer_text.get(), self.price_text.get())

			self.clear_text()
			self.populate_list()

		except SyntaxError:
			print("Syntax error adding item")

	def remove_item(self):
		# remove item from db (selected from listbox)
		try:
			db.remove(self.selected_item[0])
			self.clear_text()
			self.populate_list()
		except ValueError:
			print("Couldn't remove item from db")

	def update_item(self):
		# update selected item from listbox from db
		db.update(self.selected_item[0],
		          self.transaction_text.get(),
		          self.customer_text.get(),
		          self.retailer_text.get(),
		          self.price_text.get()
		)
		self.clear_text()


if __name__ == "__main__":

	# Instantiate database object
	db = Database('store.db')

	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()
