from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    db_name = "mydatabase.db"

    def __init__(self, window):
        self.wind = window
        self.wind.title("Products Aplication")

        #creating a new frame
        frame = LabelFrame(self.wind, text = "Register a New Product")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Name Input
        Label(frame, text = "Name: "). grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #Price Input
        Label(frame, text = "Price: ").grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #Button add product
        ttk.Button(frame, text = "Save Product", command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

        #table
        self.tree = ttk.Treeview(height=10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading("#0", text = "Name", anchor = CENTER)
        self.tree.heading("#1", text = "Price", anchor = CENTER)

        #Output Messages
        self.messages = Label(text = "", fg = "blue")
        self.messages.grid(row = 3, columnspan = 2, sticky = W + E)

        #Buttons 
        ttk.Button(text = "Delete", command = self.delet_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = "Edit", command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)

        self.get_products()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):
        #cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
            #quering data
        query = "SELECT * FROM misproductos ORDER BY name Desc"
        db_rows = self.run_query(query)
            #filling data
        for row in db_rows:
            self.tree.insert("", 0, text = row[1], values = row[2])

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=0

    def add_product(self):
        if self.validation():
            query = "INSERT INTO misproductos VALUES(NULL, ?, ?)"
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.messages["text"] = "Product {} added Successfully".format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.messages["text"] = "Name And Price are Required"
        self.get_products()

    def delet_product(self):
        self.messages["text"] = ""
        try:
            self.tree.item(self.tree.selection())["text"][0]
        except IndexError as e:
            self.messages["text"] = "Please select a record"
            return
        self.messages["text"] = ""
        name = self.tree.item(self.tree.selection())["text"]
        query = "DELETE FROM misproductos WHERE name = ?"
        self.run_query(query, (name, ))
        self.messages["text"] = "Record {} delete successfully".format(name)
        self.get_products()

    def edit_product(self):
        self.messages["text"] = ""
        try:
            self.tree.item(self.tree.selection())["text"][0]
        except IndexError as e:
            self.messages["text"] = "Please select a record"
            return
        name = self.tree.item(self.tree.selection())["text"]
        old_price = self.tree.item(self.tree.selection())["values"][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = "Edit Product"

        #Old Name
        Label(self.edit_wind, text = "Old Name").grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable =StringVar(self.edit_wind, value = name), state = "readonly").grid(row = 0, column = 2)

        #New Name
        new_name = Label(self.edit_wind, text = "New Name: ").grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        #Old Price
        Label(self.edit_wind, text = "Old Price").grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = "readonly").grid(row = 2, column = 2)

        #New Price
        new_price = Label(self.edit_wind, text = "New Price").grid(row = 3, column = 1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        #Button Update
        Button(self.edit_wind, text = "Update", command=lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)

    def edit_records(self, new_name, name, new_price, old_price):
        query = "UPDATE misproductos SET name = ?, price = ? WHERE name = ? AND price = ?"
        parameters = (new_name, new_price, name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.messages["text"] = "Update {} Successfully".format(name)
        self.get_products()

if __name__ == "__main__":
    window = Tk()
    aplication = Product(window)
    window.mainloop()