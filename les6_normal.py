# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = float(health)
        self.damage = float(damage)
        self.armor = float(armor)
    def _calculate_damage(self, damage, armor):
        return(damage // armor)
    def attack(self, health, damage):
        return(health - damage)

class Player(Person):
    pass
class Enemy(Person):
    pass

def values_player():
    player = {'name': 'player', 'health': '105', 'damage': '20', 'armor': '1.4'}
    name, health, damage, armor = list(player.values())
    player = Player(name, health, damage, armor)
    return player

def values_enemy():
    enemy = {'name': 'enemy', 'health': '80', 'damage': '30', 'armor': '1.2'}
    name, health, damage, armor = list(enemy.values())
    enemy = Enemy(name, health, damage, armor)
    return enemy

def start():
    #Функции необязательны, но я решил повторить используя функции
    player = values_player()
    enemy = values_enemy()
    #Определяем health и урон(по функции) из класса, потому, что будем вычитать урон пока, кто то не проиграет
    player_health = player.health
    enemy_health = enemy.health
    while player_health > 0 or enemy_health > 0:
        player_health = enemy.attack(player_health, enemy._calculate_damage(enemy.damage, player.armor))
        if player_health <= 0:
            print('Победил {}, осталось {} hp'.format(enemy.name, round(enemy_health, 2)))
            break
        enemy_health = player.attack(enemy_health, player._calculate_damage(player.damage, enemy.armor))
        if enemy_health <= 0:
            print('Победил {}, осталось {} hp'.format(player.name, round(player_health, 2)))
            break
start()

