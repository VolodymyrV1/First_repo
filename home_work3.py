from datetime import datetime

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


