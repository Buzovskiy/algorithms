import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_867_transpose_matrix.algorithm")
Solution = algorithm.Solution


class TestTransposeMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(self.solution.transpose(matrix), expected)

    def test_example2(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(self.solution.transpose(matrix), expected)

    def test_single_row(self):
        self.assertEqual(self.solution.transpose([[1, 2, 3]]), [[1], [2], [3]])

    def test_single_column(self):
        self.assertEqual(self.solution.transpose([[1], [2], [3]]), [[1, 2, 3]])

    def test_negative_values(self):
        matrix = [[-1, 0], [10, -9]]
        expected = [[-1, 10], [0, -9]]
        self.assertEqual(self.solution.transpose(matrix), expected)


if __name__ == "__main__":
    unittest.main()
