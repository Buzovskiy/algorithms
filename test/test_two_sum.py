import unittest
from app.leetcode import two_sum


class TwoSumTestCase(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum.Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum.Solution().twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum.Solution().twoSum([3, 3], 6), [0, 1])
