# default module
import unittest

class TestFirstClass(unittest.TestCase):

    def test_split_by_default(self):
        return 'Python Testing'.split()

    def test_split_by_comma(self):
        
        actual = 'open,high,low,close'.split(',')
        expected = ['open', 'high', 'low', 'close']
        self.assertEqual(actual, expected)

        return 'open,high,low,close'.split(',')

    def test_split_by_hash(self):
        return 'summer#time#vibes'.split('#')


if __name__ == '__main__':
    obj = TestFirstClass()
    assert obj.test_split_by_default() == ['Python','Testing']
    assert obj.test_split_by_comma() == ['open','high','low','close']
    assert obj.test_split_by_hash() == ['summer','time','vibes']