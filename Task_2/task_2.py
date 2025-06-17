import random

MIN_ALLOWED_NUMBER = 1
MAX_ALLOWED_NUMBER = 1000

def get_numbers_ticket(min_val: int, max_val: int, quantity: int):
    try:
        if (
            min_val < MIN_ALLOWED_NUMBER
            or max_val > MAX_ALLOWED_NUMBER
            or min_val > max_val
            or quantity < 1
            or quantity > (max_val - min_val + 1)
        ):
            raise ValueError

        return sorted(random.sample(range(min_val, max_val + 1), quantity))

    except ValueError:
        print("Wrong parameters.")
        return list()

if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)