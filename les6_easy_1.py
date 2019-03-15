# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def brake(self):
        print('Машина {} {} стоит!'.format(self.name, self.color))
    def drive(self):
        print('Машина {} {} цвета едет со скоростью {}!'.format(self.name, self.color, self.speed))
    def turn(self, direction):
        print('Машина {} {} цвета повернула {}'.format(self.name, self.color, direction))

class SportCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def brake(self):
        print('Машина {} {} стоит!'.format(self.name, self.color))
    def drive(self):
        print('Машина {} {} цвета едет со скоростью!'.format(self.name, self.color, self.speed))
    def turn(self, direction):
        print('Машина {} {} цвета повернула {}'.format(self.name, self.color, direction))

class WorkCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def brake(self):
        print('Машина {} {} стоит!'.format(self.name, self.color))
    def drive(self):
        print('Машина {} {} цвета едет со скоростью!'.format(self.name, self.color, self.speed))
    def turn(self, direction):
        print('Машина {} {} цвета повернула {}'.format(self.name, self.color, direction))

class PoliceCar:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def brake(self):
        print('Машина {} {} стоит!'.format(self.name, self.color))
    def drive(self):
        print('Машина {} {} цвета едет со скоростью!'.format(self.name, self.color, self.speed))
    def turn(self, direction):
        print('Машина {} {} цвета повернула {}'.format(self.name, self.color, direction))



def start():
    while True:
        do = {
             1: TownCar,
             2: SportCar,
             3: WorkCar,
             4: PoliceCar
        }

        choice = input('Выберите тип автомобиля:\n'
                   '=========================================\n'
                   '1. TownCar\n'
                   '2. SportCar\n'
                   '3. WorkCar\n'
                   '4. PoliceCar\n'
                   '5. Выход\n\n')
        try:
            if int(choice) != 0 and int(choice) <= 4:
                data = input('Введите значения скорости, цвета, название машины через пробел: ')
                speed, color, name = data.split()
                if len(data.split()) == 3 and int(speed) >= 0:
                    type = do.get(int(choice))
                    car = type(speed, color, name)
                    if int(speed) == 0:
                        car.brake()
                    else:
                        car.drive()
                        car.turn('Налево')
            else:
                if int(choice) == 5:
                    print('Вы вышли из программы!')
                    break
        except ValueError:
            print('Введите корректные значения!')
        except TypeError:
            print('Введите корректные значения!')
start()

# def start():
#     try:
#         data = input('Введите значения скорости, цвета, название ание машины через пробел: ')
#         speed, color, name = data.split()
#         if len(data.split()) != 3 or int(speed) < 0:
#             print('Вы ввели некорректные значения!')
#             return
#         # direction = input('Введите направление движения машины: ')
#         towncar = TownCar(speed, color, name)# как реаализовать словарь меню для классов?
#         if int(speed) == 0:
#             towncar.brake()
#         elif int(speed) > 0:
#             towncar.drive()
#     except ValueError:
#         print('Вы ввели некорректные значения!')
#
# if __main__ = '__main__': start()



