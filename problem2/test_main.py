import unittest

import main from caesar

class TestCaesarFunction(unittest.TestCase):

    def test_caesar_with_offset_3(self):
        self.assertEqual(caesar(3, "abc"), "def")

    def test_caesar_with_offset_2(self):
        self.assertEqual(caesar(2, "alta"), "cnvc")

    def test_caesar_with_offset_10(self):
        self.assertEqual(caesar(10, "alterraacademy"), "kvdobbkkmknowi")

    def test_caesar_with_offset_1_wraparound(self):
        self.assertEqual(caesar(1, "abcdefghijklmnopqrstuvwxyz"), "bcdefghijklmnopqrstuvwxyza")

    def test_caesar_with_large_offset_wraparound(self):
        self.assertEqual(caesar(1000, "abcdefghijklmnopqrstuvwxyz"), "mnopqrstuvwxyzabcdefghijkl")

if __name__ == '__main__':
    unittest.main()
