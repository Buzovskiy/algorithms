import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_832_flipping_an_image.algorithm")
Solution = algorithm.Solution


class TestFlippingAnImage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        self.assertEqual(self.solution.flipAndInvertImage(image), expected)

    def test_example2(self):
        image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        expected = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        self.assertEqual(self.solution.flipAndInvertImage(image), expected)

    def test_single_zero(self):
        self.assertEqual(self.solution.flipAndInvertImage([[0]]), [[1]])

    def test_single_one(self):
        self.assertEqual(self.solution.flipAndInvertImage([[1]]), [[0]])


if __name__ == "__main__":
    unittest.main()
