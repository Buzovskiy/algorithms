import importlib
import unittest

algorithm = importlib.import_module("app.leetcode.lc_896_monotonic_array.algorithm")
Solution = algorithm.Solution


class TestMonotonicArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.isMonotonic([1, 2, 2, 3]))

    def test_example2(self):
        self.assertTrue(self.solution.isMonotonic([6, 5, 4, 4]))

    def test_example3(self):
        self.assertFalse(self.solution.isMonotonic([1, 3, 2]))

    def test_equal_values(self):
        self.assertTrue(self.solution.isMonotonic([2, 2, 2]))

    def test_single_value(self):
        self.assertTrue(self.solution.isMonotonic([1]))

    def test_decrease_then_increase(self):
        self.assertFalse(self.solution.isMonotonic([5, 4, 4, 6]))


if __name__ == "__main__":
    unittest.main()
