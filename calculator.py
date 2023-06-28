import tkinter as tk
from tkinter import *

#initializing tkinter + basic setup
t = Tk()
t.geometry("700x700")
t.title("Calculator")

#initializing first input entry field
input1 = tk.Entry()
input1.pack()

#initializes second entry field
input2 = tk.Entry()
input2.pack()

#output - modified by the following functions
output_text = StringVar()
Output = tk.Label(textvariable=output_text)
Output.pack()

#sets first and second input (to be used in functions)
def getValues():
    x = float(input1.get())
    y = float(input2.get())
    return x, y

#multiplication function
def multiply():
    try:
        x, y = getValues()
        output_text.set(x * y)
    except ValueError:
        output_text.set("Invalid input")

#division function
def divide():
    try:
        x, y = getValues()
        output_text.set(x / y)
    except ValueError:
        output_text.set("Invalid input")

#addition function
def add():
    try:
        x, y= getValues()
        output_text.set(x + y)
    except ValueError:
        output_text.set("Invalid input")

#subtraction function
def subtract():
    try:
        x, y = getValues()
        output_text.set(x - y)
    except ValueError:
        output_text.set("Invalid input")


#multiplication button
multiplication_button = tk.Button(text = "Multiply", command=multiply)
multiplication_button.pack()

#division button
division_button = tk.Button(text = "Divide", command=divide)
division_button.pack()

#addition button
addition_button = tk.Button(text = "Add", command=add)
addition_button.pack()

#subtraction button
subtraction_button = tk.Button(text = "Subtract", command=subtract)
subtraction_button.pack()


#runs tkinter window
t.mainloop()