class Animals():
    def __init__(self, tail, wool, paw):
        self.tail = tail
        self.wool = wool
        self.paw = paw


class Dog(Animals):
    def __init__(self, tail, wool, paw, ball):
        Animals.__init__(self, tail, wool, paw)
        self.tail = True
        self.wool = True
        self.paw = 4
        self.ball = ball


cebek = Dog(tail=True, wool=True, paw=4, ball=5)


class Cat(Animals):
    def __init__(self, tail, wool, paw, meal):
        Animals.__init__(self, tail, wool, paw)
        self.tail = True
        self.wool = True
        self.paw = 4
        self.meal = meal


catlovan = Cat(tail=True, wool=True, paw=4, meal=True)


class Chicken(Animals):
    def __init__(self, tail, wool, paw, eggs):
        Animals.__init__(self, tail, wool, paw)
        self.tail = False
        self.wool = False
        self.paw = 2
        self.eggs = eggs


chika = Chicken(tail=False, wool=False, paw=2, eggs=4)
