def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
#print_params(a,b) вызов не выводится
print_params(b=25)
print_params(c = [1,2,3])


values_list = [1, 'string', True]
values_dict = {'a': 2, 'b': 'str', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, False]

print_params(*values_list_2, 42)