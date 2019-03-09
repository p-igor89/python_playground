# TODO: Create new list with symbols and sorted it
old_list = (8, 7, 6, 5, 4, 3, 3, 3, 4, 6)
new_l = sorted(old_list)
print(new_l)

# TODO: Create dict with int -> str like {6: '6'}, and print their in pairs
dict1 = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six'}

for key, value in dict1.items():
    print(key, value)

# TODO: Create tuple with any ten fractional numbers and find max and min value in this tuple
t = (1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0)
print('Max value in tuple is: ' + str(max(t)))
print('Min value in tuple is: ' + str(min(t)))

# TODO: Create new list with sum two exist lists
num1 = [2, 3, 4]
num2 = [4, 5, 6]

sum_result = map(lambda x1, x2: x1 + x2, num1, num2)
print(list(sum_result))

# TODO: Create list with three words, compare all words in one line that we have readable text like: 'Europe -> Ukraine -> Lviv'
_list = ['Europe', 'Ukraine', 'Lviv']
new_list = ' -> '.join(_list)
new = []
print(new_list)

# TODO: Take the string "/bin:/usr/bin:/usr/local/bin" and split by symbols ":"
old_str = '/bin:/usr/bin:/usr/local/bin'
new_str = old_str.replace(':', ' ')
print(new_str)

# TODO: Create list from 1 to 100 and print in console number number which is divisible by seven
new_list = [i for i in range(1, 100) if i % 7 == 0]
print(new_list)

# TODO: Create matrix any numbers 3x4, first print all strings, later all columns
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

for col in range(len(matrix)):
    for string in range(len(matrix[col])):
        print(matrix[col][string], end=' ')
    print('\n')

for string in range(len(matrix[col])):
    for col in range(len(matrix)):
        print(matrix[col][string], end=' ')
    print('\n')

# TODO: Create object and use for, print object and this index

obj = [1, 'fix', False, None, {1: 'dict'}, (5, 6, 7)]
for i in obj:
    print(obj.index(i), ' = ', i)

# TODO: Create new list with three parameters like 'to-delete' and another one, delete from all values like 'to-delete'
some_data = ['to-delete', '1', 'to-delete', '2asd', '3dd', '4', 'to-delete', '5']
new_data = [i for i in some_data if i != 'to-delete']
print(new_data)

# TODO: Go from 1 to 10 and vice versa (from 10 to 1) and print
old_list = [i for i in range(1, 11)]
new_list = list(reversed(old_list))
print(new_list)

_list = []
for i in range(10, 0, -1):
    _list.append(i)

print(_list)
