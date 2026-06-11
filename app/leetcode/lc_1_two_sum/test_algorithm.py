import unittest
from app.leetcode.lc_1_two_sum import algorithm


class TwoSumTestCase(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(algorithm.Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(algorithm.Solution().twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(algorithm.Solution().twoSum([3, 3], 6), [0, 1])

    def test_two_sum_enhanced(self):
        self.assertEqual(algorithm.Solution().two_sum_enhanced([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(algorithm.Solution().two_sum_enhanced([3, 2, 4], 6), [1, 2])
        self.assertEqual(algorithm.Solution().two_sum_enhanced([3, 3], 6), [0, 1])

    def test_two_sum_two_sum_best(self):
        self.assertEqual(algorithm.Solution().two_sum_best([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(algorithm.Solution().two_sum_best([3, 2, 4], 6), [1, 2])
        self.assertEqual(algorithm.Solution().two_sum_best([3, 3], 6), [0, 1])
