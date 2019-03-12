# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл(запросить подтверждение удаления)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.abspath(dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def cp():
    if not file:
        print("Необходимо указать имя существующего файла вторым параметром")
        return
    elif not os.path.isfile(file):
        print("Указанный файл не существует, скопировать нельзя. Укажите существующий файл вторым параметром!")
        return
    cp_file = os.path.basename(file) + '.bak'
    shutil.copy(cp_file, cp_file)
    print('Файл успешно создан {}'.format(cp_file))
def rm():
    if not file:
        print("Необходимо указать имя существующего файла вторым параметром!")
        return
    elif not os.path.isfile(file):
        print("Указанный файл не существует, удалить нельзя. Укажите существующий файл вторым параметром!")
        return
    q = input('Введите Y для удаления файла {}: '.format(os.path.abspath(file)))
    if q == 'Y':
        os.remove(file)
        print('Файл успешно удален {}'.format(file))
    else:
        print('Файл не был удален {}'.format(cp_file))

def cd():
    if not cd_name:
        print("Необходимо указать путь до директории вторым параметром!")
        return
    dir = os.path.abspath(cd_name)
    if os.path.exists(dir) == False:
        print('Вы ввели несуществующую директорию')
        return
    dir_new = os.chdir(dir)
    print('Новая директория: {}'.format(os.path.abspath(cd_name)))
    print('Новая текущая директория скрипта: {} '.format(os.path.abspath(os.getcwd())))


def ls():
    print('Полный путь к текущей директории: {}'.format(os.path.abspath(os.getcwd())))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    cd_name = sys.argv[2]
except IndexError:
    cd_name = None

try:
    file = sys.argv[2]
except IndexError:
    file = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")