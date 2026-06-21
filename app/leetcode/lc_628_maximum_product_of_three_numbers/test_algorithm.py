import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_628_maximum_product_of_three_numbers.algorithm")
Solution = algorithm.Solution

class TestMaximumProductOfThreeNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.maximumProduct([1, 2, 3]), 6)

    def test_example2(self):
        self.assertEqual(self.solution.maximumProduct([1, 2, 3, 4]), 24)

    def test_example3(self):
        self.assertEqual(self.solution.maximumProduct([-1, -2, -3]), -6)

    def test_two_negative_numbers(self):
        self.assertEqual(self.solution.maximumProduct([-10, -10, 5, 2]), 500)

if __name__ == "__main__":
    unittest.main()
