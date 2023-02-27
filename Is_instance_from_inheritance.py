import unittest


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        # super().append(string)


class TestStringListOnly(unittest.TestCase):

    def test_slo_is_instance(self):
        slo = StringListOnly()
        y = type(slo)
        print(y)
        self.assertIsInstance(slo, StringListOnly)
        self.assertIsInstance(slo, list)

