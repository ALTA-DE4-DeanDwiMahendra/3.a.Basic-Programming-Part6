import unittest
from main import compare

class TestCompareFunction(unittest.TestCase):

    def test_1(self):
        self.assertEqual(compare("AKA", "AKASHI"), "AKA")

    def test_2(self):
        self.assertEqual(compare("KANGOORO", "KANG"), "KANG")

    def test_3(self):
        self.assertEqual(compare("KI", "KIJANG"), "KI")

    def test_4(self):
        self.assertEqual(compare("KUPU-KUPU", "KUPU"), "KUPU")

    def test_5(self):
        self.assertEqual(compare("ILALANG", "ILA"), "ILA")
        
if __name__ == '__main__':
    unittest.main()