# Functions can be nested

def pretty_print(arg):
    def print_start():
        print('-' * 8)
        print('*' * 8)

    print_start()
    print(arg)
    print_start()


pretty_print(12)
