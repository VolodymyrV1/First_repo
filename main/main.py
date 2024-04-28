import random


def get_number_random(x, y, v):
    list_numbers = []
    try:
        range_list = list(range(x, y))
        list_numbers += range_list
        winer_numbers = sorted(random.sample(list_numbers, k=v))
        return winer_numbers
    except ValueError:
        return ('Wrong corect numbers.')

x = 1
y = 50
v = 6
print(get_number_random(x, y, v))
