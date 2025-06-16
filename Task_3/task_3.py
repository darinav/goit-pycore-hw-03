import re

normalization_pattern = r"[^\d+]"

def normalize_phone(phone_number: str):
    normalized_phone = re.sub(normalization_pattern, "", phone_number)
    if normalized_phone.startswith("+"):
        return normalized_phone
    elif normalized_phone.startswith("380"):
        return f"+{normalized_phone}"
    else:
        return f"+38{normalized_phone}"

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери:", sanitized_numbers)