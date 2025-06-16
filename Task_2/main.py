import random

MIN_ALLOWED_NUMBER = 1
MAX_ALLOWED_NUMBER = 1000

def get_numbers_ticket(min_val: int, max_val: int, quantity: int):
    try:
        if (min_val < MIN_ALLOWED_NUMBER or max_val > MAX_ALLOWED_NUMBER
                or quantity < min_val or quantity > max_val):
            raise ValueError
        return sorted(random.sample(range(min_val, max_val + 1), quantity))
    except ValueError:
        print("Wrong parameters.")
        return list()

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)