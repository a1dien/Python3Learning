class Swimmable:
    def __init__(self, name):
        print('Method init() of Swimmable')
        self.name = name

    def greetings(self):
        print(f'Hello! My name is {self.name} and I can swim')

    def swim(self):
        print('I\'m swimming')


class Walkable:
    def __init__(self, name):
        print('Method init() of Walkable')
        self.name = name

    def greetings(self):
        print(f'Hello! My name is {self.name} and I can walk')

    def walk(self):
        print('I\'m walking')


class Flyable:
    def __init__(self, name):
        print('Method init() of Flyable')
        self.name = name

    def greetings(self):
        print(f'Hello! My name is {self.name} and I can fly')

    def fly(self):
        print('I\'m flying')


class GameCharacter(Walkable, Flyable,Swimmable): #Prior
    def __init__(self, name):
        print('Method init() of GameCharacter')
        self.name = name
        Flyable.__init__(self,name)
        Walkable.__init__(self,name)
        Swimmable.__init__(self,name)

    # def greetings(self):
    #     print(f'Hello! My name is {self.name}')


james = GameCharacter('James')
james.greetings()
james.swim()
james.walk()
james.fly()

# print(isinstance(james, Walkable))
# print(isinstance(james, Swimmable))
# print(isinstance(james, Flyable))
# print(isinstance(james, GameCharacter))
# print(isinstance(james, object))

