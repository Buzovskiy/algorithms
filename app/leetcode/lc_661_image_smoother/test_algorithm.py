import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_661_image_smoother.algorithm")
Solution = algorithm.Solution


class TestImageSmoother(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(self.solution.imageSmoother(img), expected)

    def test_example2(self):
        img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
        expected = [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
        self.assertEqual(self.solution.imageSmoother(img), expected)

    def test_single_cell(self):
        self.assertEqual(self.solution.imageSmoother([[42]]), [[42]])

    def test_single_row(self):
        self.assertEqual(self.solution.imageSmoother([[1, 2, 3]]), [[1, 2, 2]])

    def test_single_column(self):
        self.assertEqual(self.solution.imageSmoother([[1], [2], [3]]), [[1], [2], [2]])


if __name__ == "__main__":
    unittest.main()
