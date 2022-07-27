from random import randint
from tkinter import *
from tkinter.messagebox import showinfo
from symbols_for_password import symbols_for_password


class Window(Frame):
    def __init__(self, window):
        super().__init__(window)

        self.password = ""

        self.label_information = Label(window, text="Enter count symbol for password", font=("Arial", 10))
        self.label_information.pack(pady=6)


        self.count_symbol_for_password_filed = Entry(window, width=20)
        self.count_symbol_for_password_filed.pack(pady=10)

        self.label_information = Button(window, text="generate password", command=self.generator_password,
                                        font=("Arial", 10))
        self.label_information.pack(pady=6)


    def generator_password(self):
        try:
            self.get_value_from_input_box = int(self.count_symbol_for_password_filed.get())
            self.password = ''

            if self.get_value_from_input_box > len(symbols_for_password):
                showinfo("Message", "Please enter count symbol for password only 1 to 2048")

            for i in range(self.get_value_from_input_box):
                self.password = f'{self.password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'

                with open(file="save_password.txt",mode="w") as file:
                    file.write(self.password)


        except Exception as exception:
            showinfo("Message", "Please Enter only number")


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("generator password".upper())
        self.geometry("250x200")
        self.resizable(False, False)


if __name__ == '__main__':
    app = App()
    window = Window(app)
    app.mainloop()
