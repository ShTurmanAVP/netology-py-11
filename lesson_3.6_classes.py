
class Animals:
    # где правильно объявлять атрибуты, здесь или в инит?
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

    def __init__(self, size, weight):
        super().__init__(size, weight)
        self.properties.append('can_fly')

    def fly(self, distance):
        self.weight /= 1.01 * distance


cow = Mammals('large', 200)
goat = Mammals('medium', 50)
sheep = Mammals('medium', 60)
pig = Mammals('medium', 100)

duck = Birds('small', 4)
chicken = Birds('small', 5)
goose = Birds('small', 7)

print(cow.legs_number, cow.size)
# Если изменять атрибут-список, то он изменится у всех объектов, будучи объявленым в теле класса, а не в инит.
# С числами этого не происходит. Почему так?
cow.lst.append('wow')
cow.properties.append('wow')
print(cow.lst, cow.properties)
print(goat.lst, goat.properties)