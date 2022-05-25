#!/usr/bin/env python
# coding: utf8
# импорты модулей
import os
import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application")

# путь где лежат файлы
path = "C:/Users/*****/Desktop/file_is_less_1_KB"
icon = "C:/Users/*****/Desktop/file_is_less_1_KB/icon.txt"
data = []
gmail = "gmail_2022@gmail.com"

with open(icon, "r", encoding='utf-8') as file:
    for line in file:
        print(line, end="")

print("\n Search for empty files that have 0.0 KB \n")
# смотрит в пути файла читает содержимое папки записывает
# размер файла если он меньше тогда добавляется в массив
for root, dirs, files in os.walk(path):
    for dir in dirs:
        for f1le in files:
            stat_info = os.stat(f1le)
            if stat_info.st_size < 1000:
                data.append(f1le)
        else:
            break
# str_a вытаскивает из массива данные и подставляет сиволы и пробелы
# и условия если массив не пустой а с данными тогда отправь иначе вывод то что нет данных
# Msg это win32com для отправка по почте Outlook
# To - кому | Subject - заголовок | Body - тело письма | Send - отправка
str_a = "\n -- ".join(data)
if data != []:
    Msg = outlook.CreateItem(0)
    Msg.To = gmail
    Msg.Subject = "Subject"
    Msg.Body = f"Hello, the check showed that these files are empty or they were uploaded incorrectly : \n\n -- {str_a} \n"
    Msg.Send()
    print(f" File is less 1 KB: \n -- {str_a}\n\n Dirs:\n -- {dir}\n")
    print(f" I'm sending this to the post office {gmail} \n ")
else:
    print(" No empty files to send \n")
