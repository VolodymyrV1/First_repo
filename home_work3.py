from datetime import datetime
import random

#Exs_1

def get_days_from_today(date):
    date_format = datetime.strptime(date, '%Y-%m-%d')
    current_day = datetime.today()
    delta_days = (date_format - current_day).days
    if delta_days <= 0:
        delta_days_modul = 0
        delta_days_modul += abs(delta_days)
        print(f'This date was {delta_days_modul} days ago.')
    else:
        print(f'This date will be in {delta_days} days.')

date = input('Enter your date YYYY-MM-DD: ')
get_days_from_today(date)

''''''
print('-' *60) #split
''''''
#Exs_2

def get_number_random(x, y, v):
    a = []
    range_list = list(range(x, y))
    a += range_list
    winer_numbers = random.sample(a, k=6)
    print(f'Winners are people who have numbers {sorted(winer_numbers)}.')

x = 1
y = 50
v = 6
get_number_random(x, y, v)


