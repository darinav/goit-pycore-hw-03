import unittest
from Task_2.task_2 import get_numbers_ticket

class TestTask2(unittest.TestCase):
    def test_valid_parameters(self):
        numbers = get_numbers_ticket(1, 49, 6)
        self.assertEqual(len(numbers), 6)
        self.assertEqual(numbers, sorted(numbers))
        self.assertEqual(len(set(numbers)), 6)
        self.assertTrue(all(1 <= n <= 49 for n in numbers))

    def test_invalid_parameters(self):
        self.assertEqual(get_numbers_ticket(0, 10, 5), [])
        self.assertEqual(get_numbers_ticket(1, 10, 20), [])
        self.assertEqual(get_numbers_ticket(1, 1001, 1), [])

if __name__ == '__main__':
    unittest.main()
