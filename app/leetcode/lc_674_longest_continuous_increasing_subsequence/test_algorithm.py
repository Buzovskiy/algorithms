import importlib
import unittest

algorithm = importlib.import_module(
    "app.leetcode.lc_674_longest_continuous_increasing_subsequence.algorithm"
)
Solution = algorithm.Solution


class TestLongestContinuousIncreasingSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findLengthOfLCIS([1, 3, 5, 4, 7]), 3)

    def test_example2(self):
        self.assertEqual(self.solution.findLengthOfLCIS([2, 2, 2, 2, 2]), 1)

    def test_single_element(self):
        self.assertEqual(self.solution.findLengthOfLCIS([10]), 1)

    def test_entire_array_increasing(self):
        self.assertEqual(self.solution.findLengthOfLCIS([1, 2, 3, 4, 5]), 5)

    def test_reset_after_decrease(self):
        self.assertEqual(self.solution.findLengthOfLCIS([5, 1, 2, 3, 0, 4, 5, 6]), 4)


if __name__ == "__main__":
    unittest.main()
