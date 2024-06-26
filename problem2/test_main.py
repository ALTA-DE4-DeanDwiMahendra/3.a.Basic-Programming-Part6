import unittest
from main import caesar

class TestCaesar(unittest.TestCase):

    def test_caesar(self):
        self.assertEqual(caesar(3, "abc"), "def")
        self.assertEqual(caesar(2, "alta"), "cnvc")
        self.assertEqual(caesar(10, "alterraacademy"), "kvdobbkkmknowi")
        self.assertEqual(caesar(1, "abcdefghijklmnopqrstuvwxyz"), "bcdefghijklmnopqrstuvwxyza")
        self.assertEqual(caesar(1000, "abcdefghijklmnopqrstuvwxyz"), "mnopqrstuvwxyzabcdefghijkl")

if __name__ == '__main__':
    unittest.main()