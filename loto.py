import random
class Card:
    def __init__(self, name):
        self.name = name
        self.bag = [i for i in range(1, 91)]
        self.count_barrels = 15 #суммарное количество боченков в билете
        self.s1, self.s2, self.s3 = self.create_barrels()
        self.p1, self.p2, self.p3 = self.gen_position()

    #функция взять все 15 боченков из сумки
    def get_barrels(self):
        x = random.sample(self.bag, self.count_barrels)
        return x
    def get_bag(self):
        return(self.bag)
    def gen_position(self):
        # позиция в строке куда вставлять значения, иначе пусто ' '
        p1 = random.sample(range(0, 8), self.count_barrels // 3)
        p2 = random.sample(range(0, 8), self.count_barrels // 3)
        p3 = random.sample(range(0, 8), self.count_barrels // 3)
        p1.sort()
        p2.sort()
        p3.sort()
        return p1, p2, p3
    def empty_string(self):
        empty_string = ['' for _ in range(9)]
        return empty_string
    def create_barrels(self):
        i = 0
        s1, s2, s3 = [], [], []
        q = self.get_barrels()
        while i < len(q):
            if i < 5:
                s1.append(q[i])
            elif i >= 5 and i < 10:
                s2.append(q[i])
            else:
                s3.append(q[i])
            i += 1
        s1.sort()
        s2.sort()
        s3.sort()
        return s1, s2, s3
    def create_lines_card(self, p, s):
        str = self.empty_string()
        i, j = 0, 0
        while i < len(str):
            if i in p:
                str[i] = s[j]
                j += 1
            i += 1
        return str
    #красивый вывод билетов
    def ticket(self):
        line = ['-'*10 + self.name + '-'*10, self.create_lines_card(self.p1, self.s1),
                self.create_lines_card(self.p2, self.s2),
                self.create_lines_card(self.p3, self.s3), '-'*35]
        return(line)
    #рабочая версия
    def ticket_lines(self):
        return [self.create_lines_card(self.p1, self.s1),
                self.create_lines_card(self.p2, self.s2),
                self.create_lines_card(self.p3, self.s3)]


class Game():
    def __init__(self, p_ticket, c_ticket):
        self.player = p_ticket
        self.computer = c_ticket

    def SportLoto(self):
        #количество боченков на карточках
        count_computer = 15
        count_player = 15
        player = self.player
        computer = self.computer
        bag = [i for i in range(1, 91)]
        while True:
            barrel = bag.pop(random.randint(0, len(bag)-1))
            print('Новый боченок: {}. Осталось {}'.format(barrel, len(bag)))
            for x in range(5):
                print(player[x])
            for y in range(5):
                print(computer[y])
            if len(bag) < 1:
                return 'Мешок пуст!!!'
            answer = input('y/n/q - зачеркнуть цифру?')
            answer = answer.lower()
            while len(answer) == 0 or answer not in 'ynq':
                print('Ответ не распознан!')
                print('Новый боченок: {}. Осталось {}'.format(barrel, len(bag)))
                for x in range(5):
                    print(player[x])
                for y in range(5):
                    print(computer[y])
                answer = input(' y/n/q - зачеркнуть цифру?')
                answer = answer.lower()
            if answer == 'q':
                print('Вы  вышли из игры')
                break
            elif answer == 'y':
                operator = False
                for x in range(1, 4):
                    if barrel in player[x]:
                        operator = True
                        player[x][player[x].index(barrel)] = '-'
                        count_player -= 1
                    if barrel in computer[x]:
                        computer[x][computer[x].index(barrel)] = '-'
                        count_computer -= 1
                if operator:
                    if count_player < 1:
                        print('Игрок выиграл!')
                        break
                    elif count_computer < 1:
                        print('Компьютер выиграл!')
                        break
                else:
                    print('Игрок проиграл! Такого числа нет на карточке!')
                    break
            elif answer == 'n':
                operator = False
                for x in range(1, 4):
                    if barrel in player[x]:
                        operator = True
                        print('Игрок проиграл, в карточке есть число {}'. format(barrel))
                    if barrel in computer[x]:
                        computer[x][computer[x].index(barrel)] = '-'
                        count_computer -= 1
                if operator:
                    break
                if count_player < 1:
                    print('Игрок выиграл!')
                    break
                elif count_computer < 1:
                    print('Компьютер выиграл!')
                    break
if __name__ == '__main__':
    p = Card('Карточка игрока')
    c = Card('Карточка компьютера')
    game = Game(p.ticket(), c.ticket())
    game.SportLoto()