import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_883_projection_area_of_3d_shapes.algorithm")
Solution = algorithm.Solution


class TestProjectionAreaOf3DShapes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.projectionArea([[1, 2], [3, 4]]), 17)

    def test_example2(self):
        self.assertEqual(self.solution.projectionArea([[2]]), 5)

    def test_example3(self):
        self.assertEqual(self.solution.projectionArea([[1, 0], [0, 2]]), 8)


if __name__ == "__main__":
    unittest.main()
