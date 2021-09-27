from app import add, users
from unittest.mock import patch
'''
expected = 30
act = add(10,20)
if expected != act:
	raise Exception("test failted for 10,20")
'''
import unittest
class AddTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
	    print("SIGN")

	@classmethod
	def tearDownClass(self):
		print("SIGNOUT") 

	def setUp(self):
		print("test started")

	def tearDown(self):
		print("test ended")

	@patch('app.get_user')
	def test_users(self, mock_get_user):
		mock_get_user.return_value=200
		expected = 200
		act = users()
		self.assertEqual(expected, act)

	def test_str1_str2(self):
		expected="str1str2"
		act = add("str1", "str2")
		self.assertEqual(expected, act)
		

	def test_10_20(self):
		expected = 30
		act = add(10,20)
		self.assertEqual(expected, act)

	def test_10_str1(self):
		expected = None
		act = add(10,"str1")
		self.assertEqual(expected, act)

