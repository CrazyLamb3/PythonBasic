# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


# Склеивание строк, не тру вариант
# fruits = ['яблоко', 'банан', 'киви', 'арбуз']
# i = 0
# while i < len(fruits):
#     print('{}.'.format(i+1) + '{:>10}'.format(fruits[i]))
#     i+=1

# Без склеивания строк, it's true
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
i = 0
while i < len(fruits):
    print('{}.{:>10}'.format(i+1, fruits[i]))
    i += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = [1, 2, 'Dima', 3.05, 'python', 'random']

b = [0, 'python', 2, 'Dima']

print('1-ый список:', a)
print('2-ой список:', b)

for i in b:
    for y in a:
        # print('b=', y, 'a=', i)
        if i == y:
            a.remove(y)
print('Из 1-го списка удалили элементы, которые есть во 2-ом списке', a)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
#  если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два

import random
l1 = []
l2 = []
n = int(input('Введите число элементов списка:'))

for i in range(n):
    y = random.randint(1, 100)
    l1.append(y)
    if y % 2 == 0:
        y = y / 4
    else:
        y = y * 2
    l2.append(y)

print('Исходный список:', l1)

print('Новый список:', l2)
