from datetime import datetime, date, timedelta

DATE_FORMAT = "%Y-%m-%d"

def get_days_from_today(date_str: str):
    """Return the number of days between ``date_str`` and today.

    If ``date_str`` has incorrect format the function returns ``None``.
    Only the date part of ``datetime`` objects is used in the calculation so
    the time of day does not affect the result.
    """
    try:
        today = date.today()
        target_date = datetime.strptime(date_str, DATE_FORMAT).date()
    except ValueError:
        return None

    return (today - target_date).days

def get_valid_int(prompt: str, min_val: int, max_val: int):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                raise ValueError
            return value
        except ValueError:
            print(f"Please enter a number between {min_val} and {max_val}.")

def run():
    print("Input desired date")
    year = get_valid_int("Enter year (1–9999): ", min_val=1, max_val=9999)
    month = get_valid_int("Enter month (1–12): ", min_val=1, max_val=12)

    while True:
        day = get_valid_int("Enter day (1–31): ", min_val=1, max_val=31)
        try:
            datetime_obj = date(year, month, day)
            date_str = datetime_obj.strftime(DATE_FORMAT)
            print(f"\nYou entered: {date_str} "
                  f"\nTime until that date: {get_days_from_today(date_str)} days")
            break
        except ValueError:
            print("Invalid day for the given month/year. Try again.")

def test_days_until():
    today = date.today()
    future_date = today + timedelta(days=1)
    past_date = today - timedelta(days=1)

    days_to_future = get_days_from_today(future_date.strftime(DATE_FORMAT))
    days_to_past = get_days_from_today(past_date.strftime(DATE_FORMAT))
    assert days_to_future < 0, f"Expected negative timedelta, got {days_to_future}"
    assert days_to_past > 0, f"Expected positive timedelta, got {days_to_past}"

if __name__ == "__main__":
    test_days_until()
    print("✅ Test passed!")
    run()