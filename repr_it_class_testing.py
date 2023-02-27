import unittest

class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __lt__(self, other):
        return len(self.string) < len(other.string)

class TestDoc(unittest.TestCase):
    pass

obj = Doc('pankaj')
obj1  = Doc("ramayan")
print(obj.__init__("mukesh"))
print(obj.__repr__())
print(obj.__lt__(obj1))