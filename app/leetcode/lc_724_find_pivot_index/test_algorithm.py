import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_724_find_pivot_index.algorithm")
Solution = algorithm.Solution


class TestFindPivotIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.pivotIndex([1, 7, 3, 6, 5, 6]), 3)

    def test_example2(self):
        self.assertEqual(self.solution.pivotIndex([1, 2, 3]), -1)

    def test_example3(self):
        self.assertEqual(self.solution.pivotIndex([2, 1, -1]), 0)


if __name__ == "__main__":
    unittest.main()
