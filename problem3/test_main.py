import unittest

import main from array_unique

class TestArrayUniqueFunction(unittest.TestCase):

    def test_unique_elements_case_1(self):
        self.assertEqual(array_unique([1, 2, 3, 4], [1, 3, 5, 10, 16]), [2, 4])

    def test_unique_elements_case_2(self):
        self.assertEqual(array_unique([10, 20, 30, 40], [5, 10, 15, 59]), [20, 30, 40])

    def test_unique_elements_case_3(self):
        self.assertEqual(array_unique([1, 3, 7], [1, 3, 5]), [7])

    def test_unique_elements_case_4(self):
        self.assertEqual(array_unique([3, 8], [2, 8]), [3])

    def test_no_unique_elements(self):
        self.assertEqual(array_unique([1, 2, 3], [3, 2, 1]), [])

if __name__ == '__main__':
    unittest.main()
