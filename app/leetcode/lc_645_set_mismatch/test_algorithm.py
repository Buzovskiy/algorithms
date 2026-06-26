import unittest

from app.leetcode.lc_645_set_mismatch.algorithm import Solution


class TestSetMismatch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findErrorNums([1, 2, 2, 4]), [2, 3])

    def test_example2(self):
        self.assertEqual(self.solution.findErrorNums([1, 1]), [1, 2])

    def test_missing_first_number(self):
        self.assertEqual(self.solution.findErrorNums([2, 2]), [2, 1])

    def test_missing_last_number(self):
        self.assertEqual(self.solution.findErrorNums([1, 2, 3, 3]), [3, 4])


if __name__ == "__main__":
    unittest.main()
