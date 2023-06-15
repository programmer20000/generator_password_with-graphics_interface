import csv
import json
import os

import openpyxl

from .utils import message_create_file

directory_path = os.path.join('C:', 'Users', os.getlogin(), 'Downloads')


def create_text_file(password: str = ''):  # todo: this function  is for creating text file
    with open(file=f'{directory_path}/yours_password.txt', mode='w') as file:
        file.write(password)
        return message_create_file(filename=file.name)


def create_json_file(dictionary: dict):  # todo: this function  is for creating json file
    with open(file=f'{directory_path}/yours_password.json', mode='w') as file:
        json.dump(dictionary, file, indent=4)
        return message_create_file(filename=file.name, file_path=directory_path)


def create_excel_file(dictionary: dict):  # todo: this function  is for creating Excel file
    book = openpyxl.Workbook()
    sheet = book.active

    sheet['A1'] = 'DATA AND TIME'
    sheet['B1'] = 'PASSWORD'
    row = 2

    for key, value in dictionary.items():
        sheet[row][0].value = key
        sheet[row][1].value = value
        row += 1

    book.save(f'{directory_path}/yours_password.xlsx')

    return message_create_file(filename='yours_password.xlsx', file_path=directory_path)


def create_csv_file(date_time: str = '', password: str = ''):  # todo: this function  is for creating csv file
    with open(file=f'{directory_path}/yours_password.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerows([
            ('DATA AND TIME', 'PASSWORD'),
            [date_time, password]
        ])
        return message_create_file(filename=file.name,file_path=directory_path)
