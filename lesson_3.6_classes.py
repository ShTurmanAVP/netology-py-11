
class Animals:
    legs_number = 4
    lst = []

    def __init__(self, size, weight):
        self.size = size
        self.weight = weight
        self.properties = ['has_spine', 'has_neural_system']

    def eat(self):
        self.weight *= 1.02


class Mammals(Animals):
    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('feed_children_with_milk')

    def feed(self):
        self.weight /= 1.02


class Birds(Animals):
    legs_number = 2
    wings_number = 2

    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('can_fly')
        self.properties.append('lays_eggs')

    def fly(self, distance):
        self.weight /= 1.01 * distance


class Duck(Birds):
    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('can_swim')


class Chicken(Birds):
    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('produce_eggs')


class Goose(Birds):
    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('can_swim')
        self.properties.append('produce_fluff')


class Cow(Mammals):
    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('produce_beef')
        self.properties.append('has_horns')


class Goat(Mammals):
    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('produce_goat')
        self.properties.append('has_horns')


class Sheep(Mammals):
    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('produce_mutton')
        self.properties.append('produce_wool')


class Pig(Mammals):
    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('produce_pork')
        self.properties.append('produce_fat')


cow = Cow('large', 200)
goat = Goat('large', 200)
sheep = Sheep('large', 200)
pig = Pig('large', 200)

duck = Duck('small', 4)
chicken = Chicken('small', 5)
goose = Goose('small', 7)

print(cow.legs_number, cow.size)
# Если изменять атрибут-список, то он изменится у всех объектов, будучи объявленым в теле класса, а не в инит.
# С числами этого не происходит. Почему так?
cow.lst.append('wow')
print('Список, объявленный в теле класса, изменился у всех экземпляров класса:', cow.lst, goat.lst)
cow.properties.append('wow')
print('Список, объявленный в методе инициализации, изменился только у конкретного экземпляра:', cow.properties,
      goat.properties)
print('Почему?')
