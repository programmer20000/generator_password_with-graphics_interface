import tkinter as tk
from datetime import datetime
from random import randint
from tkinter import ttk
from tkinter.messagebox import showinfo

from symbols_for_password import symbols_for_password


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.date_and_time = datetime.now()

        self.label_information = ttk.Label(text="Enter count symbol for password", font=("Arial", 10)).pack(pady=16)
        self.count_symbols_for_password = ttk.Entry(width=20).pack(pady=6)
        self.button_generate_password = ttk.Button(text="generate password", width=20,
                                                   command=self.generator_password).pack(pady=10)

    def generator_password(self):
        self.get_value_from_input_filed = int(self.count_symbols_for_password.get())

        self.password = ''

        if self.get_value_from_input_filed > len(symbols_for_password):
            showinfo("Please enter count symbol for password only 1 to 2048")

        for i in range(self.get_value_from_input_filed):
            self.password = f'{self.password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'
        self.date_created_password = f"{self.date_and_time}{self.password}"

        print(self.date_created_password)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('generator password'.upper())
        self.geometry('240x240')
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
