import random

def get_number_random(x, y, v):
    a = []
    range_list = list(range(x, y))
    a += range_list
    winer_numbers = random.sample(a, k=6)
    print(sorted(winer_numbers))

x = 1
y = 50
v = 6
get_number_random(x, y, v)