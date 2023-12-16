from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("C:/Users/MSI/Downloads/calculator-icon_34473.ico")

global method
method = ""

def calculate():
    if len(method) != 0:
        second_num = display.get()
        display.delete(0, END)
        if method == "add":
            total = float(f_num) + float(second_num)
        if method == "sub":
            total = float(f_num) - float(second_num)
        if method == "mul":
            total = float(f_num) * float(second_num)
        if method == "divi":
            if second_num != "0":
                total = float(f_num) / float(second_num)
            else:
                total = "Error"
        display.insert(0, total)


def press(num):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(num))


def clear():
    display.delete(0, END)


def add():
    global f_num
    global method
    first_num = display.get()
    f_num = first_num
    method = "add"
    display.delete(0, END)


def sub():
    global f_num
    global method
    first_num = display.get()
    f_num = first_num
    method = "sub"
    display.delete(0, END)


def mul():
    global f_num
    global method
    first_num = display.get()
    f_num = first_num
    method = "mul"
    display.delete(0, END)


def divide():
    global f_num
    global method
    first_num = display.get()
    f_num = first_num
    method = "divi"
    display.delete(0, END)


num0 = Button(root, text="0", padx=25, pady=25, command=lambda: press(0))
num1 = Button(root, text="1", padx=25, pady=25, command=lambda: press(1))
num2 = Button(root, text="2", padx=25, pady=25, command=lambda: press(2))
num3 = Button(root, text="3", padx=25, pady=25, command=lambda: press(3))
num4 = Button(root, text="4", padx=25, pady=25, command=lambda: press(4))
num5 = Button(root, text="5", padx=25, pady=25, command=lambda: press(5))
num6 = Button(root, text="6", padx=25, pady=25, command=lambda: press(6))
num7 = Button(root, text="7", padx=25, pady=25, command=lambda: press(7))
num8 = Button(root, text="8", padx=25, pady=25, command=lambda: press(8))
num9 = Button(root, text="9", padx=25, pady=25, command=lambda: press(9))
clear = Button(root, text="clear", padx=25, pady=25, command=clear)
add_button = Button(root, text="+", padx=25, pady=25, command=lambda: add())
sub_button = Button(root, text="-", padx=25, pady=25, command=lambda: sub())
mulitply_button = Button(root, text="x", padx=25,
                         pady=25, command=lambda: mul())
division_button = Button(root, text="/", padx=25,
                         pady=25, command=lambda: divide())
equal_button = Button(root, text="=", padx=25, pady=25,
                      command=lambda: calculate())
display = Entry(root, width=45)

num1.grid(row=3, column=0)
num2.grid(row=3, column=1)
num3.grid(row=3, column=2)

num4.grid(row=2, column=0)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)

num7.grid(row=1, column=0)
num8.grid(row=1, column=1)
num9.grid(row=1, column=2)

display.grid(row=0, column=0, columnspan=4, pady=10)

num0.grid(row=4, column=0,)

equal_button.grid(row=4, column=2, columnspan=1)
clear.grid(row=4, column=1)

add_button.grid(row=4, column=3)
sub_button.grid(row=3, column=3)
mulitply_button.grid(row=2, column=3)
division_button.grid(row=1, column=3)

root.mainloop()