import unittest


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)


class unittest(unittest.TestCase):
    def test_append_string(self):
        x = StringListOnly()
        x.append('pankaj')
        self.assertIn('pankaj', x)

    def test_append_not_string_should_raise_error(self):
        a = ['1', '2']
        # b = True
        y = StringListOnly()
        self.assertRaises(TypeError, y.append, a)

# class Animals:
# 	# Initializing constructor
# 	def __init__(self):
# 		self.legs = 4
# 		self.domestic = True
# 		self.tail = True
# 		self.mammals = True
#
# 	def isMammal(self):
# 		if self.mammals:
# 			print("It is a mammal.")
#
# 	def isDomestic(self):
# 		if self.domestic:
# 			print("It is a domestic animal.")
#
# class Dogs(Animals):
# 	def __init__(self):
# 		super().__init__()
#
# 	def isMammal(self):
# 		super().isMammal()
#
# class Horses(Animals):
# 	def __init__(self):
# 		super().__init__()
#
# 	def hasTailandLegs(self):
# 		if self.tail and self.legs == 4:
# 			print("Has legs and tail")
#
#
# # Driver code
# Tom = Dogs()
# Tom.isMammal()
# Bruno = Horses()
# Bruno.hasTailandLegs()
