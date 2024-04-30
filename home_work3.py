#Exs_1
def get_days_from_today(date):
    try:
        date_format = datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.today().date()
        delta_days = (date_format - today_date).days
        return delta_days
    except ValueError:
        text_mesage = input('Enter your date in format YYYY-MM-DD: ')
        return get_days_from_today(text_mesage)
    
date = input('Enter your date YYYY-MM-DD: ')
print(get_days_from_today(date))

''''''
print('-' *60) #split
''''''


#Exs_2
import random

def get_numbers_ticket(min, max, quantity):
    list_numbers = []
    try:
        if min < 1 or max > 1000 or min > max:
            return list_numbers
        if (max - min) < quantity:
            return list_numbers 
        else:
            range_list = list(range(min, max))
            list_numbers += range_list
            winer_numbers = sorted(random.sample(list_numbers, k=quantity))
            return winer_numbers
    except ValueError:
        return list_numbers


min = int(input('Enter your min number: '))
max = int(input('Enter your max number: '))
quantity = int(input('Enter your quantity: '))
print(get_numbers_ticket(min, max, quantity))

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


