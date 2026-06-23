import importlib
import unittest

algorithm = importlib.import_module("app.leetcode.lc_643_maximum_average_subarray_i.algorithm")
Solution = algorithm.Solution


class TestMaximumAverageSubarrayI(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertAlmostEqual(
            self.solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4),
            12.75,
            places=5,
        )

    def test_example2(self):
        self.assertAlmostEqual(self.solution.findMaxAverage([5], 1), 5.0, places=5)

    def test_all_negative_numbers(self):
        self.assertAlmostEqual(
            self.solution.findMaxAverage([-1, -12, -5, -6, -50, -3], 2),
            -5.5,
            places=5,
        )


if __name__ == "__main__":
    unittest.main()
