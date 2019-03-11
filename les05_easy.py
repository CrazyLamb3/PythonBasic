
import os
import shutil

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dirs():
    listdir = list(os.listdir())
    result = [i for i in listdir if os.path.isdir(i) == True]
    return('Список папок текущей директории: {}'.format(result))

if __name__ == '__main__': print(list_dirs())

#Список файлов и папок для задания normal
def list_files():
    return ('Список файлов и папок текущей директории:{}'.format(os.listdir()))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
if __name__ == '__main__':
    file = os.path.basename(__file__) + '.bak'
    shutil.copy(__file__, file)

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir(n):
    i = 1
    while i <= n:
        namedir = 'dir_'+str(i)
        os.mkdir(namedir)
        i+= 1
    print('Было создано {} директории(ий)'.format(n))

def remove_dir(n, dirs):
    if n == 0:
        return 'Директорий не найдено'
    else:
        for i in dirs:
            os.rmdir(i)
        return 'Было удалено {} директорий'.format(n)

def start_easy():
    while True:
        try:
            listdir = os.listdir()
            dirs = list(filter(lambda x: 'dir_' in x, listdir))
            print('В каталоге есть {} директорий для удалений'.format(len(dirs)))
            print('Список папок, в которых в имени присутствует dir_:{}'.format(dirs))
            q = int(input("Введите 1 - сделать n-ое количество директорий dir_ n\n"
                          "Введите 2 - удалить n-ое количество директорий dir_n\n"
                          "Введите 10 - для выхода\n"
                          "----------------\n"
                          "Ваш выбор:"))
        except ValueError:
            print('Введите корректное значению меню:')
            continue
        if q == 1:
            n = int(input('Введите количество директорий, которые хотите создать:'))
            make_dir(n)
        elif q == 2:
            n = len(dirs)
            print(remove_dir(n, dirs))
        elif q == 10:
            print('Вы решили выйти из программы')
            break
        else:
            print('Введите корректное значение меню:')

if __name__ == '__main__': start_easy()


