from itertools import count

number = input("Введите по порядку, без пробелов, элементы кортежа:")
s = tuple(number)
f = set(s)
for i in f:
    print(f'Количество {i} = {s.count(i)}')


