import unittest
from mymathlib import addition


class Mytest(unittest.TestCase):


	"""test de la fonction addition"""


	def test_addition(self):
		self.assertEqual(4, addition(2,2))


	def test_multiplication(self):
		self.assertEqual(0, addition(0,2))



if __name__ == "__main__":
	unittest.main()



