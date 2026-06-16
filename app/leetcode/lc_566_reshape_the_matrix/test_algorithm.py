import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_566_reshape_the_matrix.algorithm")
Solution = algorithm.Solution

class TestReshapeMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: mat = [[1,2],[3,4]], r = 1, c = 4
        # Output: [[1,2,3,4]]
        mat = [[1, 2], [3, 4]]
        r, c = 1, 4
        expected = [[1, 2, 3, 4]]
        self.assertEqual(self.solution.matrixReshape(mat, r, c), expected)

    def test_example2(self):
        # Example 2: mat = [[1,2],[3,4]], r = 2, c = 4
        # Output: [[1,2],[3,4]]
        mat = [[1, 2], [3, 4]]
        r, c = 2, 4
        expected = [[1, 2], [3, 4]]
        self.assertEqual(self.solution.matrixReshape(mat, r, c), expected)

    def test_reshape_impossible(self):
        mat = [[1, 2, 3], [4, 5, 6]]
        r, c = 3, 3
        # 6 elements cannot fit in 3x3 (9 spots)
        expected = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(self.solution.matrixReshape(mat, r, c), expected)

    def test_one_to_many(self):
        mat = [[1, 2, 3, 4]]
        r, c = 2, 2
        expected = [[1, 2], [3, 4]]
        self.assertEqual(self.solution.matrixReshape(mat, r, c), expected)

    def test_many_to_one(self):
        mat = [[1, 2], [3, 4]]
        r, c = 4, 1
        expected = [[1], [2], [3], [4]]
        self.assertEqual(self.solution.matrixReshape(mat, r, c), expected)

if __name__ == "__main__":
    unittest.main()
