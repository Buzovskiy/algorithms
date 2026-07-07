import importlib
import unittest

algorithm = importlib.import_module("app.leetcode.lc_746_min_cost_climbing_stairs.algorithm")
Solution = algorithm.Solution

class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.minCostClimbingStairs([10, 15, 20]), 15)

    def test_example2(self):
        self.assertEqual(
            self.solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
            6,
        )

    def test_two_steps(self):
        self.assertEqual(self.solution.minCostClimbingStairs([0, 0]), 0)

if __name__ == "__main__":
    unittest.main()
