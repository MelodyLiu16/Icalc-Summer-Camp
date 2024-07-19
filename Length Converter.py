from tkinter import *
import tkinter as tk
from tkinter import ttk
import re


class LengthConverter:
    def __init__(self):
        self.lengths = dict()
        with open("Lengths.py") as file:
            for line in file:
                line = line.rstrip("\n")
                length, rate = line.split(":")
                self.lengths[length] = float(rate)
        print(self.lengths)

    def convert(self, from_length, to_length, amount):
        initial_amount = amount
        if from_length != "inch":
            amount = amount / self.lengths[from_length]
        amount = round(amount * self.lengths[to_length], 3)
        return amount


my_converter = LengthConverter()
print(my_converter.convert("inch", "cm", 50))


class App(Tk):
    def __init__(self, converter):
        Tk.__init__(self)
        self.my_converter = converter
        self.config(bg="pink")
        self.geometry("500x500")

        self.title = Label(self, text="Length Converter")
        self.title.config(font=("Perpetua 20 bold"))
        self.title.place(x=150, y=5)

        self.entry_box = Entry(self, bd=3, justify=CENTER)
        self.entry_box.place(x=175, y=120)

        self.from_length_list = StringVar(self)
        self.from_length_list.set("cm")
        self.to_length_list = StringVar(self)
        self.to_length_list.set("inch")

        font = "Perpetua 12"
        self.option_add("*TCombobox*Listbox.font", font)
        self.from_length_dropdown = ttk.Combobox(
            self,
            textvariable=self.from_length_list,
            value=list(self.my_converter.lengths.keys()),
        )
        self.to_length_dropdown = ttk.Combobox(
            self,
            textvariable=self.to_length_list,
            value=list(self.my_converter.lengths.keys()),
        )
        self.from_length_dropdown.place(x=100, y=80)
        self.to_length_dropdown.place(x=250, y=80)

        self.result = Label(self, text="")
        self.result.config(font=("Perpeuta 12 bold"))
        self.result.place(x=200, y=200)

        self.convert_button = Button(
            self, text="Convert", bg="red", command=self.do_convert
        )
        self.convert_button.config(font="Mistral 10")
        self.convert_button.place(x=200, y=250)

    def do_convert(self):
        amount = float(self.entry_box.get())
        from_len = self.from_length_dropdown.get()
        to_len = self.to_length_dropdown.get()
        converted_amount = self.my_converter.convert(from_len, to_len, amount)
        self.result.config(text=str(converted_amount))


my_converter = LengthConverter()
App(my_converter)
mainloop()
