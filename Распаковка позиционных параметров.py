def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1. Функция с параметрами по умолчанию
print_params()
print_params(b='25')
print_params(c=[1, 2, 3])
print_params(c='Some string')

# 2. Распаковка параметров
values_list = [42, 'строка из списка', False]
values_dict = {'a': 99, 'b': 'из словаря', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
