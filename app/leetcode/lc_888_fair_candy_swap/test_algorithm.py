import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_888_fair_candy_swap.algorithm")
Solution = algorithm.Solution


class TestFairCandySwap(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.fairCandySwap([1, 1], [2, 2]), [1, 2])

    def test_example2(self):
        self.assertEqual(self.solution.fairCandySwap([1, 2], [2, 3]), [1, 2])

    def test_example3(self):
        self.assertEqual(self.solution.fairCandySwap([2], [1, 3]), [2, 3])


if __name__ == "__main__":
    unittest.main()
