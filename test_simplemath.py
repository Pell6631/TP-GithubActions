import unittest
from simplemath import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(33, 36)
        self.assertEqual(result, 69)
    def test_substraction(self):
        result = SimpleMath.substraction(45, 6)
        self.assertEqual(result, 39)