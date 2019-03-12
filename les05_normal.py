# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
from les05_easy import list_files

def go_to_folder(folder):
    if os.path.isdir(folder) == True:
        return 'Вы зашли в папку {}'.format(os.path.abspath(folder))
    elif os.path.isabs(folder) == False:
        return 'Указанная папка {} не существует в директории {}'.format(folder, os.getcwd())

def create_folder(folder):
    if os.path.isdir(folder) == False:
        os.mkdir(folder)
        return 'Папка была создана: {}'.format(folder)
    elif os.path.isdir(folder) == True:
        return 'Папка с именем {} уже существует'.format(folder)

def delete_folder(folder):
    if os.path.isdir(folder) == True:
        os.rmdir(folder)
        return 'Папка была удалена:{}'.format(folder)
    elif os.path.isdir(folder) == False:
        return 'Папка с именем {} не существует'.format(folder)

def start_normal():
    while True:
        try:
            q = int(input("1 - Перейти в папку\n"
                          "2 - Просмотреть содержимое текущей папки\n"
                          "3 - Удалить папку\n"
                          "4 - Создать папку\n"
                          "Введите 100 - для выхода\n"
                          "----------------\n"
                          "Ваш выбор:"))
        except ValueError:
            print('Введите корректное значение меню:')
            continue
        if q == 1:
            try:
                folder = input('Введите название папки в которую хотите перейти:')
                print(go_to_folder(folder))
            except ValueError:
                print('Введите корректное название папки!')
        elif q == 2:
            print(list_files())
        elif q == 3:
            try:
                folder = input('Введите название папки, которую хотите удалить:')
                print(delete_folder(folder))
            except ValueError:
                print('Введите корректное название папки!')
        elif q == 4:
            try:
                folder = input('Введите название папки, которую хотите создать:')
                print(create_folder(folder))
            except ValueError:
                print('Введите корректное название папки!')
        elif q == 100:
            print('Вы вышли из программы')
            break
        else:
            print('Введите корректное значение меню:')

start_normal()


