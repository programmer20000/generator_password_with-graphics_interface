import os
from tkinter.messagebox import showinfo

from pyperclip import copy


def copy_password(password: str = ''):
    # todo: This function is for copy password in clipboard
    copy(password)
    return showinfo('Message', 'Yours password successful copy'.upper())


def message_create_file(filename: str = '', file_path=None):
    # todo: This function is for information user about successful create file

    for file in os.listdir(file_path):
        if os.path.exists(file.startswith('yours_password')):
            return showinfo('Message', f'file with name {filename} is created with successful'.upper())


def open_directory(file_path=None):
    os.startfile(file_path)
