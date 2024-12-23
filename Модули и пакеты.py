# fake_math.py
def divide(first, second):
    if second == 0:
        return 'Ошибка'
    return first / second

# true_math.py
from math import inf

def divide(first, second):
    if second == 0:
        return inf
    return first / second

# module_4_1.py
from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)
