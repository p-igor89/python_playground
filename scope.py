# TODO: Local scope
def scoped_function(arg):
    value = arg * 10
    print(value)


scoped_function(2)


# TODO: Returning something
def return_some(input_value):
    calc = input_value - 7
    return calc


print(return_some(10))

# TODO: Global scope
SOME_VAR = 'value!'


def print_var():
    print(SOME_VAR)  # value


print_var()


# TODO: Can not modify global variable
def modify_var():
    try:
        SOME_VAR += '12'
    except UnboundLocalError as e:
        print('Error', e)


modify_var()
print(SOME_VAR)

# But you can mutate it
GLOBAL_LIST = []


def append_to_list(item):
    print('Adding', item)
    GLOBAL_LIST.append(item)


append_to_list(1)
append_to_list(2)
print(GLOBAL_LIST)
