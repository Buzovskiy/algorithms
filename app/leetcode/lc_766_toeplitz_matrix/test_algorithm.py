import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_766_toeplitz_matrix.algorithm")
Solution = algorithm.Solution


class TestToeplitzMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 1, 2, 3],
            [9, 5, 1, 2],
        ]
        self.assertTrue(self.solution.isToeplitzMatrix(matrix))

    def test_example2(self):
        self.assertFalse(self.solution.isToeplitzMatrix([[1, 2], [2, 2]]))

    def test_single_row(self):
        self.assertTrue(self.solution.isToeplitzMatrix([[1, 2, 3]]))

    def test_single_column(self):
        self.assertTrue(self.solution.isToeplitzMatrix([[1], [2], [3]]))

    def test_larger_non_toeplitz_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 1, 9],
            [7, 4, 1],
        ]
        self.assertFalse(self.solution.isToeplitzMatrix(matrix))


if __name__ == "__main__":
    unittest.main()
