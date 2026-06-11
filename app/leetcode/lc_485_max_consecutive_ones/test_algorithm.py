import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_485_max_consecutive_ones.algorithm")

Solution = algorithm.Solution

class TestMaxConsecutiveOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: nums = [1,1,0,1,1,1], Output: 3
        nums = [1, 1, 0, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)

    def test_example2(self):
        # Example 2: nums = [1,0,1,1,0,1], Output: 2
        nums = [1, 0, 1, 1, 0, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 2)

    def test_all_ones(self):
        nums = [1, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 4)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_empty_list(self):
        # Constraints say 1 <= nums.length, but let's be safe
        nums = []
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_alternating(self):
        nums = [1, 0, 1, 0, 1, 0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 1)

    def test_single_one(self):
        nums = [1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 1)

    def test_single_zero(self):
        nums = [0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

if __name__ == "__main__":
    unittest.main()
