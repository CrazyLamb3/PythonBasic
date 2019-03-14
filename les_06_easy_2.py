# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.info()
    def info(self):
        print('Тип автомобиля Car!')
    def brake(self):
        print('Машина {} {} стоит!'.format(self.name, self.color))
    def drive(self):
        print('Машина {} {} цвета едет со скоростью {}!'.format(self.name, self.color, self.speed))
    def turn(self, direction):
        print('Машина {} {} цвета повернула {}'.format(self.name, self.color, direction))

class TownCar(Car):
    def info(self):
        print('Тип автомобиля TownCar!')

class SportCar(Car):
    def info(self):
        print('Тип автомобиля SportCar!')

class WorkCar(Car):
    def info(self):
        print('Тип автомобиля WorkCar!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed,color,name,is_police)
    def info(self):
        print('Тип автомобиля PoliceCar!')


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

