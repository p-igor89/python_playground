class Car:
    pass


c = Car()
print(c, type(c))


class Room:
    number = 'Room 34'
    floor = 4


r = Room()
r1 = Room()
print(r.number, r1.number)
print(r.floor, r1.floor)

# TODO: You can modify values:
r.number = 12
r.floor = '5 floor'
print(r.number, r1.number)
print(r.floor, r1.floor)


# TODO: Classes can have functions inside: it's colled method

class Door:
    def open(self):  # note, that self is an object
        print('self if', self)
        print('Door is opened')
        self.opened = True


d = Door()
d.open()


# TODO: Methods can accept params
class Terminal:
    def hello(self, user_name):
        print('self is the object inself', self)
        print('Hello', user_name)


t = Terminal()
t.hello('Nikita')
t.hello('Vova')


# TODO: Classes can have both methods and fields
class Window:
    is_opened = False

    def open(self):
        self.is_opened = not self.is_opened
        print('Window is now ', self.is_opened)


w = Window()
w1 = Window()

print('Initial state', w.is_opened, w1.is_opened)
w.open()
print('New state', w.is_opened, w1.is_opened)
