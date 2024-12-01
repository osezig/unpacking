def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# print_params()
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
# print_params(b = 25)
# print_params(c = [1,2,3])

values_list = [0.24, 'Жора', True]

values_dict = {'a': 1, 'b': "Жора Киллер", 'c': 0.25}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 0.33]
print_params(*values_list_2, 42)