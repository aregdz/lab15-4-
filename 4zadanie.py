#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import END, LEFT, Button, Entry, Text, Tk


def open_file():
    filename = entry.get()
    try:
        with open(filename, "r") as file:
            content = file.read()
            text.delete("1.0", END)
            text.insert("1.0", content)
    except FileNotFoundError:
        text.delete("1.0", END)
        text.insert("1.0", "Файл не найден.")


def save_file():
    filename = entry.get()
    content = text.get("1.0", END)
    with open(filename, "w") as file:
        file.write(content)


if __name__ == "__main__":
    root = Tk()
    root.title("Редактор файлов")

    entry = Entry(root, width=50)
    entry.pack(pady=5)

    text = Text(root, width=50, height=20)
    text.pack(pady=5)

    open_button = Button(root, text="Открыть", command=open_file)
    open_button.pack(side=LEFT, padx=5)

    save_button = Button(root, text="Сохранить", command=save_file)
    save_button.pack(side=LEFT, padx=5)

    root.mainloop()
