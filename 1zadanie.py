#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "ошибка: деление на ноль"
        else:
            result = "ошибка: некорректный оператор"

        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="ошибка: введите числа")

    def set_operator(op):
        operator_var.set(op)


if __name__ == "__main__":
    root = Tk()
    root.title("Калькулятор")

    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    entry1 = Entry(frame, width=10)
    entry1.pack()

    operator_var = StringVar()
    operator_var.set("+")
    operator_menu = OptionMenu(frame, operator_var, "+", "-", "*", "/")
    operator_menu.pack()

    entry2 = Entry(frame, width=10)
    entry2.pack()

    calculate_button = Button(frame, text="Вычислить", command=calculate)
    calculate_button.pack(pady=5)

    equal_label = Label(frame, text="=")
    equal_label.pack()

    result_label = Label(frame, text="")
    result_label.pack()

    root.mainloop()
