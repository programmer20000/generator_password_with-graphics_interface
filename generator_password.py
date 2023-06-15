from random import randint
from tkinter import END
from tkinter.messagebox import showinfo

import customtkinter

from symbols_for_password import symbols_for_password
from write_password_in_file import ToplevelWindow


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.create_objects()

    def create_objects(self):
        self.length_password_entry = customtkinter.CTkEntry(
            master=self,
            placeholder_text='Enter Length Password',
            font=('Arial', 12),
        )
        self.length_password_entry.grid(row=0, rowspan=2, column=0, padx=100, pady=10, sticky='nsew')

        self.generate_password_btn = customtkinter.CTkButton(
            self, text='Generate Password', command=self.generator_password
        )
        self.generate_password_btn.grid(rowspan=2, columnspan=2, padx=100, pady=20)

    def generator_password(self):  # todo: This method contain main algorithm that for generating password
        try:
            self.question_user = int(self.length_password_entry.get())

            self.password = ''

            def clear_entry():
                self.length_password_entry.delete(0, END)
                self.length_password_entry.insert(0, '0')

            if self.question_user > len(symbols_for_password):
                clear_entry()
                return showinfo(
                    'Warning', 'Please enter count symbol for password only 1 to 2048'.upper()
                )
            if self.question_user <= 1:
                clear_entry()
                return showinfo('Message', 'Your`s amount of symbols for a password is very little'.upper())

            for i in range(self.question_user):
                self.password = f'{self.password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'
            self.open_toplevel(password=self.password)

            return showinfo('Message', 'Yours password successful created'.upper())

        except ValueError:
            return showinfo('Warning', 'Please enter only number values'.upper())

    def open_toplevel(self, *, password: str):  # todo: This method is for redirecting on next window
        self.toplevel_window = None
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(
                self
            )
            self.toplevel_window.show_password(password=password)
            self.toplevel_window.place_buttons()

            # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


class App(customtkinter.CTk):
    # todo: this block of code is with configurations for window
    def __init__(self):
        super().__init__()
        self.geometry('400x200')
        self.title('Generator Password')
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')


if __name__ == '__main__':
    app = App()
    app.mainloop()
