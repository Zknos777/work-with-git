import random


class Car:
    def __init__(self, brand, model,
                 year=2000, color=(0, 0, 255)):
        """ инициализация """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.condition = {'tires': 100,
                          'engine': 100,
                          'fuel': 100,
                          'glass': 100,
                          'body': 100}

    def change_color(self, new_color):
        """ перекрасить """
        self.color = new_color

    def change_condition(self, part, value):
        if part in self.condition.keys():
            self.condition[part] = value
        else:
            print('invalid part:', part)

    def show_condition(self):
        print('Condition:')
        for part in self.condition.keys():
            print(f'{part}:\t{self.condition[part]}')

    def crash(self, level):
        print(f'crash level {level}')
        if level == 'low':
            self.condition['body'] -= random.randint(5, 20)
            self.condition['glass'] -= random.randint(0, 10)
        elif level == 'medium':
            self.condition['body'] -= random.randint(10, 40)
            self.condition['glass'] -= random.randint(5, 30)
            self.condition['engine'] -= random.randint(0, 10)
        elif level == 'high':
            self.condition['body'] -= random.randint(30, 80)
            self.condition['glass'] -= random.randint(30, 80)
            self.condition['engine'] -= random.randint(10, 50)
        elif level == 'total':
            self.condition['body'] -= random.randint(50, 95)
            self.condition['glass'] -= random.randint(50, 95)
            self.condition['engine'] -= random.randint(30, 70)

    def __str__(self):
        return f'{self.brand} {self.model}, color: {self.color}'


class Kia(Car):
    def __init__(self, model, year=2000, color=(0, 255, 0)):
        super().__init__('Kia', model, year, color)


class KiaRio(Kia):
    def __init__(self, year=2000, color=(0, 255, 0)):
        super().__init__('Rio', year, color)


if __name__ == '__main__':
    # ford = Car(brand='Ford', model='Focus', year=2005)
    # print(ford)
    # ford.change_color((255, 0, 0))
    # print(ford)
    # ford.show_condition()
    # ford.crash(random.choice(['low', 'medium', 'high', 'total']))
    # ford.show_condition()
    kia = Kia(model='Picanto', year=2010)
    print(kia)
    kia.show_condition()
    kia_rio = KiaRio()
    print(kia_rio)

    print(issubclass(KiaRio, Kia))
    print(issubclass(KiaRio, Car))

    print(isinstance(kia_rio, KiaRio))
    print(isinstance(kia_rio, Kia))
    print(isinstance(kia_rio, Car))


