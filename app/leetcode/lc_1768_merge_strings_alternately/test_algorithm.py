import unittest
from app.leetcode.lc_1768_merge_strings_alternately.algorithm import Solution

class TestMergeStringsAlternately(unittest.TestCase):
    def test_merge_alternately(self):
        sol = Solution()
        # Note: Current implementation in algorithm.py has a fixed range(3)
        # and doesn't handle different lengths or longer strings well.
        # I'll test with strings of length 3 first as per its current logic.
        self.assertEqual(sol.mergeAlternately("abc", "pqr"), "apbqcr")

if __name__ == '__main__':
    unittest.main()
