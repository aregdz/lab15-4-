#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def show_phone_number():
    selected_person = var.get()
    phone_number = people_data[selected_person]
    label.config(text=f"Номер телефона: {phone_number}")


if __name__ == "__main__":
    people_data = {
        "Иван": "123-456-789",
        "Мария": "987-654-321",
        "Алексей": "555-555-555",
    }

    root = tk.Tk()
    root.title("Информация о людях")

    var = tk.StringVar()

    max_name_length = max(len(person) for person in people_data)

    for i, person in enumerate(people_data, start=1):
        rb = tk.Radiobutton(
            root,
            text=person.ljust(max_name_length),
            variable=var,
            value=person,
            indicatoron=0,
            width=20,
            command=show_phone_number,
        )
        rb.grid(row=i, column=0, sticky=tk.W)

    label = tk.Label(root, text="Выберите человека", font=("Arial", 12))
    label.grid(row=0, column=1, padx=15, pady=(10, 0))

    phone_label = tk.Label(root, text="", font=("Arial", 12))
    phone_label.grid(
        row=len(people_data) + 1, columnspan=2, padx=15, pady=(10, 10)
    )

    root.mainloop()
