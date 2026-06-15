import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_561_array_partition.algorithm")
Solution = algorithm.Solution

class TestArrayPartition(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 4, 3, 2]
        expected = 4
        self.assertEqual(self.solution.arrayPairSum(nums), expected)

    def test_example2(self):
        nums = [6, 2, 6, 5, 1, 2]
        expected = 9
        self.assertEqual(self.solution.arrayPairSum(nums), expected)

if __name__ == "__main__":
    unittest.main()
