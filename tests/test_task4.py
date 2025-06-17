import unittest
from unittest.mock import patch
from datetime import datetime as real_datetime

from Task_4.task_4 import get_upcoming_birthdays

class TestTask4(unittest.TestCase):
    def test_get_upcoming_birthdays(self):
        fake_today = real_datetime(2024, 1, 10)
        users = [
            {"name": "John", "birthday": "1985.01.10"},  # Wednesday
            {"name": "Jane", "birthday": "1990.01.13"},  # Saturday -> Monday 15th
            {"name": "Skip", "birthday": "1999.02.01"},  # outside range
        ]
        with patch('Task_4.task_4.datetime') as mock_dt:
            mock_dt.today.return_value = fake_today
            mock_dt.strptime.side_effect = lambda d, f: real_datetime.strptime(d, f)
            result = get_upcoming_birthdays(users)
        expected = [
            {"name": "John", "congratulation_date": "2024.01.10"},
            {"name": "Jane", "congratulation_date": "2024.01.15"},
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
