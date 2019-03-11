# TODO: Constructor is called when new instance is created
class TestClass:
    def __init__(self):
        print('Constructor is called')
        print('Self is the object itself', self)


t = TestClass()
t1 = TestClass()


# TODO: Constructor can have parameters
class Table:
    def __init__(self, number_of_legs):
        print('New table has {} lags'.format(number_of_legs))


t = Table(4)
t = Table(3)


# TODO: But we need to save them into the field
class Chair:
    def __init__(self, color):
        self.color = color


c = Chair('green')
print(c, c.color)
c1 = Chair('red')
print(c1, c1.color)
print('variable c did not change', c.color)

