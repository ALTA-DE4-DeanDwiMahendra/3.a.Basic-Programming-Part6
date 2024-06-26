import unittest
from main import find_max_sum_sub_array

class TestFindMaxSumSubArray(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2]), 9)

    def test_case_2(self):
        self.assertEqual(find_max_sum_sub_array(2, [2, 3, 4, 1, 5]), 7)

    def test_case_3(self):
        self.assertEqual(find_max_sum_sub_array(2, [2, 1, 4, 1, 1]), 5)

    def test_case_4(self):
        self.assertEqual(find_max_sum_sub_array(3, [2, 1, 4, 1, 1]), 7)

    def test_case_5(self):
        self.assertEqual(find_max_sum_sub_array(4, [2, 1, 4, 1, 1]), 8)

if __name__ == '__main__':
    unittest.main()
