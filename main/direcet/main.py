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