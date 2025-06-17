from datetime import datetime, timedelta

DATE_FORMAT = "%Y.%m.%d"

def process_birthday_entry(user_bd_entry):
    today = datetime.today().date()
    congratulation_date_limit = today + timedelta(days=7)

    name = user_bd_entry["name"]
    birthday_str = user_bd_entry["birthday"]
    birthday_date = datetime.strptime(birthday_str, DATE_FORMAT).date()

    birthday_this_year = birthday_date.replace(year=today.year)
    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)

    if today <= birthday_this_year <= congratulation_date_limit:
        congratulation_date = birthday_this_year
        if congratulation_date.weekday() == 5:  # Saturday
            congratulation_date += timedelta(days=2)
        elif congratulation_date.weekday() == 6:  # Sunday
            congratulation_date += timedelta(days=1)

        return {
            "name": name,
            "congratulation_date": congratulation_date.strftime(DATE_FORMAT)
        }

    return None

def get_upcoming_birthdays(user_birthdays):
    congratulation_list = []

    for user in user_birthdays:
        result = process_birthday_entry(user)
        if result:
            congratulation_list.append(result)

    return congratulation_list

users = [
    {"name": "John Doe", "birthday": "1985.06.18"},
    {"name": "Jane Smith", "birthday": "1990.06.22"},
]

if __name__ == "__main__":
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань:", upcoming_birthdays)
