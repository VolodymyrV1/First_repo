from datetime import datetime
import random

#Exs_1

def get_days_from_today(date):
    date_format = datetime.strptime(date, '%Y-%m-%d').date()
    today_date = datetime.today().date()
    delta_days = (date_format - today_date).days
    return delta_days
    
date = input('Enter your date YYYY-MM-DD: ')
print(get_days_from_today(date))

''''''
print('-' *60) #split
''''''
#Exs_2

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


