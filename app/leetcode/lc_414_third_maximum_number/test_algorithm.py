import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_414_third_maximum_number.algorithm")
Solution = algorithm.Solution


class TestThirdMax(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: nums = [3,2,1], Output: 1
        self.assertEqual(self.solution.thirdMax([3, 2, 1]), 1)

    def test_example2(self):
        # Example 2: nums = [1,2], Output: 2
        self.assertEqual(self.solution.thirdMax([1, 2]), 2)

    def test_example3(self):
        # Example 3: nums = [2,2,3,1], Output: 1
        self.assertEqual(self.solution.thirdMax([2, 2, 3, 1]), 1)

    def test_only_one(self):
        self.assertEqual(self.solution.thirdMax([1]), 1)

    def test_duplicates(self):
        self.assertEqual(self.solution.thirdMax([1, 1, 1]), 1)
        self.assertEqual(self.solution.thirdMax([1, 2, 2]), 2)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.thirdMax([-1, -2, -3]), -3)
        self.assertEqual(self.solution.thirdMax([-1, -2]), -1)

    def test_long_list(self):
        self.assertEqual(self.solution.thirdMax([5, 2, 4, 1, 3]), 3)


if __name__ == "__main__":
    unittest.main()
