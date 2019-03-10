def fun():
    print("i'm a function")


print(fun)
print('Functions are objects', isinstance(fun, object))

# TODO: Can use variables to store functions
test = fun
test()

# TODO: Can do any actions with functions
_list = []
_list.append(fun)
print(_list)


# TODO: Can pass functions as parameters
def call_passed_functions(incoming):
    print("calling")
    incoming()
    print('Called')


call_passed_functions(fun)

# TODO: Can not call uncallable things
try:
    d = 2
    d()  # just try
except TypeError as e:
    print("it's not a function", e)

# TODO: Can check if something could be called
print(callable(len), callable(45), callable(callable))


# TODO: Can return function from a function
def return_min_function():
    return min


test = return_min_function()
min_value = test(4, 6, 7, -9, 12)
print('Min value is: ', min_value)
