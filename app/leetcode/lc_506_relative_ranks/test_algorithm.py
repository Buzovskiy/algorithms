import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_506_relative_ranks.algorithm")
Solution = algorithm.Solution

class TestRelativeRanks(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        score = [5, 4, 3, 2, 1]
        expected = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
        self.assertEqual(self.solution.findRelativeRanks(score), expected)

    def test_example2(self):
        score = [10, 3, 8, 9, 4]
        expected = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
        self.assertEqual(self.solution.findRelativeRanks(score), expected)

    def test_single_athlete(self):
        score = [10]
        expected = ["Gold Medal"]
        self.assertEqual(self.solution.findRelativeRanks(score), expected)

    def test_three_athletes(self):
        score = [1, 2, 3]
        expected = ["Bronze Medal", "Silver Medal", "Gold Medal"]
        self.assertEqual(self.solution.findRelativeRanks(score), expected)

if __name__ == "__main__":
    unittest.main()
