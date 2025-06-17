import unittest
from Task_3.task_3 import normalize_phone, raw_numbers

class TestTask3(unittest.TestCase):
    def test_normalization_examples(self):
        expected = ['+380671234567', '+380952345678', '+380441234567',
                    '+380501234567', '+380501233234', '+380503451234',
                    '+380508889900', '+380501112222', '+380501112211']
        result = [normalize_phone(num) for num in raw_numbers]
        self.assertEqual(result, expected)

    def test_existing_prefix(self):
        self.assertEqual(normalize_phone('+380123456789'), '+380123456789')

if __name__ == '__main__':
    unittest.main()
