calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    """
    Принимает строку и возвращает кортеж из:
    - длины строки,
    - строки в верхнем регистре,
    - строки в нижнем регистре.
    """
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    """
    Проверяет наличие строки в списке, игнорируя регистр.
    """
    count_calls()
    lower_string = string.lower()
    lower_list = [item.lower() for item in list_to_search]
    return lower_string in lower_list

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
