import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, 2)

def calculate_daily_return_almost(open, close):
    return (close / open - 1) * 100


class TestCalculateDailyReturn(unittest.TestCase):
    def test_positive_return(self):
        print(calculate_daily_return(349.0, 360.0))
        self.assertEqual(calculate_daily_return(349.0, 360.0), 3.16)

    def test_almost_equal(self):
        Expected = calculate_daily_return_almost(349.0, 360.0)
        print(Expected)
        message = "almost equal assertion failed"
        decimal_place = 3
        Actual = 3.1518
        self.assertAlmostEqual(Expected, Actual, decimal_place, message)

