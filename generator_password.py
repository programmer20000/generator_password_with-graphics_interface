from random import randint
from tkinter.messagebox import showwarning

import customtkinter
import pyperclip

from symbols_for_password import symbols_for_password


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.length_password_input = customtkinter.CTkEntry(self, placeholder_text='Please Enter length password')
        self.length_password_input.grid(row=0, column=0, padx=100, pady=10)

        self.show_password = customtkinter.CTkLabel(self, text='yours password ', fg_color="transparent")
        self.show_password.grid(rowspan=2, columnspan=2, padx=100, pady=10)

        self.button = customtkinter.CTkButton(self, text="CTkButton", command=self.generator_password)
        self.button.grid(rowspan=2, columnspan=2, padx=100, pady=20)

    def generator_password(self):
        try:
            self.question_user = int(self.length_password_input.get())

            self.password = ''

            if self.question_user > len(symbols_for_password):
                return showwarning('Warning', 'Please enter count symbol for password only 1 to 2048')

            for i in range(self.question_user):
                self.password = f'{self.password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'
            self.show_password.configure(text=self.password)
            pyperclip.copy(self.password)
            return showwarning('Message', 'Yours password successful copy')

        except ValueError:
            return showwarning('Warning', 'Please enter only number values')



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title('Generator Password')
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == '__main__':
    app = App()
    app.mainloop()
