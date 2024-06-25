import unittest

import main from remove_duplicates

class TestRemoveDuplicatesFunction(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(remove_duplicates([2, 3, 3, 3, 6, 9, 9]), 4)

    def test_case_2(self):
        self.assertEqual(remove_duplicates([2, 3, 4, 5, 6, 9, 9]), 6)

    def test_case_3(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 11]), 2)

    def test_case_4(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 11]), 2)

    def test_case_5(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 11, 11]), 4)

if __name__ == '__main__':
    unittest.main()
