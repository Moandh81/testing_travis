import unittest
from mymathlib import addition, multiplication, appendtolist 


class Mytest(unittest.TestCase):


	"""test de la fonction addition"""


	def test_addition(self):
		self.assertEqual(4, addition(2,2))


	def test_multiplication(self):
		self.assertEqual(0, multiplication(0,2))


	def test_appendtolist(self):
		self.assertEqual(["bonjour", "bonsoir", "bienvenue", "hello"], appendtolist("hello"))



if __name__ == "__main__":
	unittest.main()



