#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Button, Label, Tk


def change_color1():
    l1["text"] = "Красный"
    l2["text"] = "#ff0000"


def change_color2():
    l1["text"] = "Оранжевый"
    l2["text"] = "#ff7d00"


def change_color3():
    l1["text"] = "Желтый"
    l2["text"] = "#ffff00"


def change_color4():
    l1["text"] = "Зеленый"
    l2["text"] = "#00ff00"


def change_color5():
    l1["text"] = "Голубой"
    l2["text"] = "#007dff"


def change_color6():
    l1["text"] = "Синий"
    l2["text"] = "#0000ff"


def change_color7():
    l1["text"] = "Фиолетовый"
    l2["text"] = "#7d00ff"


if __name__ == "__main__":
    root = Tk()

    l1 = Label(text="")
    l2 = Label(text="")
    l1.pack()
    l2.pack()

    rainbow_colors = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ]

    b1 = Button(
        text="Изменить",
        width=15,
        height=3,
        bg=rainbow_colors[0],
        command=change_color1,
    )
    b1.pack()

    b2 = Button(
        text="Изменить",
        width=15,
        height=3,
        bg=rainbow_colors[1],
        command=change_color2,
    )
    b2.pack()

    b3 = Button(
        text="Изменить",
        width=15,
        height=3,
        bg=rainbow_colors[2],
        command=change_color3,
    )
    b3.pack()

    b4 = Button(
        text="Изменить",
        width=15,
        height=3,
        bg=rainbow_colors[3],
        command=change_color4,
    )
    b4.pack()

    b5 = Button(
        text="Изменить",
        width=15,
        height=3,
        bg=rainbow_colors[4],
        command=change_color5,
    )
    b5.pack()

    b6 = Button(
        text="Изменить",
        width=15,
        height=3,
        bg=rainbow_colors[5],
        command=change_color6,
    )
    b6.pack()

    b7 = Button(
        text="Изменить",
        width=15,
        height=3,
        bg=rainbow_colors[6],
        command=change_color7,
    )
    b7.pack()

    root.mainloop()
