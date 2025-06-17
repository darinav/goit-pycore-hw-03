import unittest
from datetime import date, timedelta

from Task_1.task_1 import get_days_from_today, DATE_FORMAT

class TestTask1(unittest.TestCase):
    def test_today(self):
        today = date.today()
        self.assertEqual(get_days_from_today(today.strftime(DATE_FORMAT)), 0)

    def test_future_and_past(self):
        today = date.today()
        future = today + timedelta(days=3)
        past = today - timedelta(days=5)
        self.assertEqual(get_days_from_today(future.strftime(DATE_FORMAT)), -3)
        self.assertEqual(get_days_from_today(past.strftime(DATE_FORMAT)), 5)

    def test_invalid_date(self):
        self.assertIsNone(get_days_from_today('invalid'))

if __name__ == '__main__':
    unittest.main()
