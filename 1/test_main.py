import unittest

from main import find_first_decimal, find_last_decimal, get_calibration_value, sum_calibration_values


class TestMain(unittest.TestCase):
    def test_find_first_decimal(self):
        self.assertEqual(find_first_decimal('abc'), None)
        self.assertEqual(find_first_decimal('1abc2'), '1')
        self.assertEqual(find_first_decimal('pqr3stu8vwx'), '3')
        self.assertEqual(find_first_decimal('a1b2c3d4e5f'), '1')
        self.assertEqual(find_first_decimal('treb7uchet'), '7')
        self.assertEqual(find_first_decimal('two1nine'), '2')
        self.assertEqual(find_first_decimal('eightwothree'), '8')
        self.assertEqual(find_first_decimal('abcone2threexyz'), '1')
        self.assertEqual(find_first_decimal('xtwone3four'), '2')
        self.assertEqual(find_first_decimal('4nineeightseven2'), '4')
        self.assertEqual(find_first_decimal('zoneight234'), '1')
        self.assertEqual(find_first_decimal('7pqrstsixteen'), '7')

    def test_find_last_decimal(self):
        self.assertEqual(find_last_decimal('abc'), None)
        self.assertEqual(find_last_decimal('1abc2'), '2')
        self.assertEqual(find_last_decimal('pqr3stu8vwx'), '8')
        self.assertEqual(find_last_decimal('a1b2c3d4e5f'), '5')
        self.assertEqual(find_last_decimal('treb7uchet'), '7')
        self.assertEqual(find_last_decimal('two1nine'), '9')
        self.assertEqual(find_last_decimal('eightwothree'), '3')
        self.assertEqual(find_last_decimal('abcone2threexyz'), '3')
        self.assertEqual(find_last_decimal('xtwone3four'), '4')
        self.assertEqual(find_last_decimal('4nineeightseven2'), '2')
        self.assertEqual(find_last_decimal('zoneight234'), '4')
        self.assertEqual(find_last_decimal('7pqrstsixteen'), '6')

    def test_get_calibration_value(self):
        self.assertEqual(get_calibration_value('abc'), 0)
        self.assertEqual(get_calibration_value('1abc2'), 12)
        self.assertEqual(get_calibration_value('pqr3stu8vwx'), 38)
        self.assertEqual(get_calibration_value('a1b2c3d4e5f'), 15)
        self.assertEqual(get_calibration_value('treb7uchet'), 77)
        self.assertEqual(get_calibration_value('two1nine'), 29)
        self.assertEqual(get_calibration_value('eightwothree'), 83)
        self.assertEqual(get_calibration_value('abcone2threexyz'), 13)
        self.assertEqual(get_calibration_value('xtwone3four'), 24)
        self.assertEqual(get_calibration_value('4nineeightseven2'), 42)
        self.assertEqual(get_calibration_value('zoneight234'), 14)
        self.assertEqual(get_calibration_value('7pqrstsixteen'), 76)

    def test_sum_calibration_values(self):
        self.assertEqual(sum_calibration_values(
            ['abc', '1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']), 142)
        self.assertEqual(sum_calibration_values(
            ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']), 281)
