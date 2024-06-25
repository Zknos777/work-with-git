import random


class Car:
    __color = (0, 0, 255)
    __year = 2000
    __condition = {'tires': 100,
                   'engine': 100,
                   'fuel': 100,
                   'glass': 100,
                   'body': 100}

    def change_year(self, year):
        if year in range(1970, 2025):
            self.__year = year


    def change_color(self, new_color):
        if all([c in range(256) for c in new_color]):
            self.__color = new_color
    def __init__(self, brand, model):
        """ инициализация """
        self.brand = brand
        self.model = model


    def change_condition(self, part, value):
        if not value in range(101):
            print('Invalid value:', value)
            return
        if part in self.__condition.keys():
            self.__condition[part] = value
        else:
            print('invalid part:', part)

    def show_condition(self):
        print('Condition:')
        for part in self.__condition.keys():
            print(f'{part}:\t{self.__condition[part]}')

    def crash(self, level):
        print(f'crash level {level}')
        if level == 'low':
            self.__condition['body'] -= random.randint(5, 20)
            self.__condition['glass'] -= random.randint(0, 10)
        elif level == 'medium':
            self.__condition['body'] -= random.randint(10, 40)
            self.__condition['glass'] -= random.randint(5, 30)
            self.__condition['engine'] -= random.randint(0, 10)
        elif level == 'high':
            self.__condition['body'] -= random.randint(30, 80)
            self.__condition['glass'] -= random.randint(30, 80)
            self.__condition['engine'] -= random.randint(10, 50)
        elif level == 'total':
            self.__condition['body'] -= random.randint(50, 95)
            self.__condition['glass'] -= random.randint(50, 95)
            self.__condition['engine'] -= random.randint(30, 70)

    def __str__(self):
        return f'{self.brand} {self.model}, color: {self.__color}'


class Kia(Car):
    def __init__(self, model, year=2000, color=(0, 255, 0)):
        super().__init__('Kia', model, year, color)


class KiaRio(Kia):
    def __init__(self, year=2000, color=(0, 255, 0)):
        super().__init__('Rio', year, color)


if __name__ == '__main__':
    ford = Car(brand='Ford', model='Focus')
    print(ford)
    ford.change_color((255, 0, 0))
    print(ford)
    ford.__color = 123
    print(ford)



