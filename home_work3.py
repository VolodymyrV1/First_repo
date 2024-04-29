#Exs_1
from datetime import datetime

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
import random

def get_number_random(x, y, v):
    list_numbers = []
    if v == 0 or x <=0 or y >50:
        return list_numbers
    else:
        range_list = list(range(x, y))
        list_numbers += range_list
        winer_numbers = sorted(random.sample(list_numbers, k=v))
        return winer_numbers

x = 1
y = 50
v = 6
print(get_number_random(x, y, v))

''''''
print('-' *60) #split
''''''


#Exs_3

import re

def normalize_phone(phone_numbers):
    for phone in phone_numbers:
        cleaned_number = re.sub(r'\D', '', phone)
        if not cleaned_number.startswith('+'):
            if cleaned_number.startswith('380'):
                cleaned_number = '+' + cleaned_number
            else:
                cleaned_number = '+38' + cleaned_number

        return cleaned_number

phone_numbers = [
"    +38(050)123-32-34"
]
print(normalize_phone(phone_numbers))


