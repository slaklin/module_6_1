class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Plant:
    def __init__(self, name, edible):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, False)


class Fruit (Plant):
    def __init__(self, name):
        super().__init__(name, True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)