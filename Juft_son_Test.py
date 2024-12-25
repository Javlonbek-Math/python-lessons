import unittest
from juft_son import juft_son
class JuftSonTest(unittest.TestCase):
    def test_juft(self):
        qiymat=juft_son([4,5,6,7,8])
        self.assertEqual(qiymat,[4,6,8])
unittest.main()

