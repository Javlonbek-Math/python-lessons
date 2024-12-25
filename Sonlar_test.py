import unittest
from sonlar import sonlar
class Son_test(unittest.TestCase):
    def test_son(self):
        self.assertEqual(sonlar(3, 5, 7),7)
        self.assertEqual(sonlar(-2,-4,-7),-2)
unittest.main()
