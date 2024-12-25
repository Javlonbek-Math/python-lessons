import unittest
from Big_letter import Big_letter
class Big_letter_test(unittest.TestCase):
    def test_big(self):
        result=Big_letter(['kitob','daftar'])
        self.assertEqual(result,['Kitob','Daftar'])

unittest.main()

    
