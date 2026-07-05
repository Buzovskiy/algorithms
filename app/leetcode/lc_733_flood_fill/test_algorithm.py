import importlib
import unittest

algorithm = importlib.import_module("app.leetcode.lc_733_flood_fill.algorithm")
Solution = algorithm.Solution


class TestFloodFill(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertEqual(self.solution.floodFill(image, 1, 1, 2), expected)

    def test_example2(self):
        image = [[0, 0, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(self.solution.floodFill(image, 0, 0, 0), expected)

    def test_single_pixel(self):
        self.assertEqual(self.solution.floodFill([[1]], 0, 0, 2), [[2]])

    def test_fill_only_connected_component(self):
        image = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
        expected = [[3, 3, 0], [3, 0, 1], [0, 1, 1]]
        self.assertEqual(self.solution.floodFill(image, 0, 0, 3), expected)


if __name__ == "__main__":
    unittest.main()
