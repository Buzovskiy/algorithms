import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_598_range_addition_ii.algorithm")
Solution = algorithm.Solution

class TestRangeAdditionII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        m = 3
        n = 3
        ops = [[2, 2], [3, 3]]
        self.assertEqual(self.solution.maxCount(m, n, ops), 4)

    def test_example2(self):
        m = 3
        n = 3
        ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
        self.assertEqual(self.solution.maxCount(m, n, ops), 4)

    def test_example3(self):
        m = 3
        n = 3
        ops = []
        self.assertEqual(self.solution.maxCount(m, n, ops), 9)

    def test_min_dimensions(self):
        m = 40000
        n = 40000
        ops = [[1, 1]]
        self.assertEqual(self.solution.maxCount(m, n, ops), 1)

if __name__ == "__main__":
    unittest.main()
