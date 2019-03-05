# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
def attack(person1, person2):
    print('Player с именем {} имеет {} health и наносит урон {} damage'.format(name1, health1, damage1))
    print('Enemy с именем {} имеет {} health и наносит урон {} damage'.format(name2, health2, damage2))
    player_health = health1 - damage2
    enemy_health = health2 - damage1
    person1.clear()
    person2.clear()
    person1 = {'name': name1, 'health': player_health, 'damage': damage1}
    person2 = {'name': name2, 'health': enemy_health, 'damage': damage2}
    print('После нападения у {} осталось {} health'.format(name1, player_health))
    print('После нападения у {} осталось {} health'.format(name2, enemy_health))

name1 = input('Введите имя player:')
name1 = name1.capitalize()
name2 = input('Введите имя enemy:')
name2 = name2.capitalize()
if name1.isalpha() and name2.isalpha():
    #определяем словари
    player = {'name': name1, 'health': 100, 'damage': 40}
    enemy = {'name': name2, 'health': 80, 'damage': 30}
    damage1 = player.get('damage')
    damage2 = enemy.get('damage')
    health1 = player.get('health')
    health2 = enemy.get('health')
    attack(player, enemy)
else:
    print('Вы не ввели данные!!!')


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def read_files(file1, file2):
    with open('player.txt', 'r') as file1:
        player = []
        for line in file1:
            i = line.strip()
            player.append(i)
    with open('enemy.txt', 'r') as file2:
        enemy = []
        for line in file2:
            i = line.strip()
            enemy.append(i)
    person1 = dict(zip(keys, player))
    person2 = dict(zip(keys, enemy))
    return person1, person2

def armor(person1, person2):
    damage12 = damage1/armor2
    damage21 = damage2/armor1
    damage12 = round(damage12, 2)
    damage21 = round(damage21, 2)
    person1.update({'damage': damage12})
    person2.update({'damage': damage21})
    return person1, person2

def attack(person1, person2):
    # person1, person2 = armor(player, enemy)
    damage1 = float(person1.get('damage'))
    damage2 = float(person2.get('damage'))
    health1 = float(person1.get('health'))
    health2 = float(person2.get('health'))
    print('Player с именем {} имеет {} health и наносит урон {} damage'.format(name1, health1, damage1))
    print('Enemy с именем {} имеет {} health и наносит урон {} damage'.format(name2, health2, damage2))
    health1 = float(health1)
    health2 = float(health2)
    while health1 > 0 or health2 > 0:
        health1 = health1 - damage2
        if health1 <= 0:
            print('Победил {}, осталось {}'.format(name2, round(health2, 2)))
            break
        health2 = health2 - damage1
        if health2 <= 0:
            print('Победил {}, осталось {}'.format(name1, round(health1, 2)))
            break

#----------------MAIN---------------
name1 = input('Введите имя player:')
name1 = name1.capitalize()
name2 = input('Введите имя enemy:')
name2 = name2.capitalize()
if name1.isalpha() and name2.isalpha():
    #определяем словари
    player = {'name': name1, 'health': 100, 'damage': 40, 'armor': 1.2}
    enemy = {'name': name2, 'health': 80, 'damage': 30, 'armor': 1.2}
else:
    print('Вы не ввели данные!!!')

#создаю лист ключей словаря
keys = []
for i in player.keys():
    keys.append(i)

with open('player.txt', 'w', encoding='UTF-8') as file1:
    for key in player:
        file1.write('{}\n'.format(player.get(key)))
with open('enemy.txt', 'w', encoding='UTF-8') as file2:
   for key in player:
        file2.write('{}\n'.format(enemy.get(key)))

#очищаю словари
player.clear()
enemy.clear()

#Игровая сессия

player, enemy = read_files(file1, file2)
name1 = player.get('name')
name2 = enemy.get('name')
damage1 = float(player.get('damage'))
damage2 = float(enemy.get('damage'))
health1 = float(player.get('health'))
health2 = float(enemy.get('health'))
armor1 = float(player.get('armor'))
armor2 = float(enemy.get('armor'))
#вычисляем новый урон и обновляем словари в функции
player, enemy = armor(player, enemy)
attack(player, enemy)