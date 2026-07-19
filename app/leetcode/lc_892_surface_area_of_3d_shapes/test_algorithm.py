import importlib
import unittest

algorithm = importlib.import_module("app.leetcode.lc_892_surface_area_of_3d_shapes.algorithm")
Solution = algorithm.Solution


class TestSurfaceAreaOf3DShapes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.surfaceArea([[1, 2], [3, 4]]), 34)

    def test_example2(self):
        self.assertEqual(
            self.solution.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
            32,
        )

    def test_example3(self):
        self.assertEqual(
            self.solution.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]),
            46,
        )

    def test_single_cube(self):
        self.assertEqual(self.solution.surfaceArea([[1]]), 6)

    def test_empty_cell(self):
        self.assertEqual(self.solution.surfaceArea([[0]]), 0)


if __name__ == "__main__":
    unittest.main()
