import unittest
from fibonacci import fibonacci
class FibonacciTest(unittest.TestCase):
    def test_true(self):
        result1=fibonacci(15, 5)
        self.assertTrue(result1)

    def test_false(self):
        result2=fibonacci(15, 11)

        self.assertFalse(result2)
unittest.main()
        

