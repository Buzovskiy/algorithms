import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_812_largest_triangle_area.algorithm")
Solution = algorithm.Solution


class TestLargestTriangleArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]

        self.assertAlmostEqual(self.solution.largestTriangleArea(points), 2.0, places=5)

    def test_example2(self):
        points = [[1, 0], [0, 0], [0, 1]]

        self.assertAlmostEqual(self.solution.largestTriangleArea(points), 0.5, places=5)


if __name__ == "__main__":
    unittest.main()
