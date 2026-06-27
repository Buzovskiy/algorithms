import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_697_degree_of_an_array.algorithm")
Solution = algorithm.Solution


class TestDegreeOfAnArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findShortestSubArray([1, 2, 2, 3, 1]), 2)

    def test_example2(self):
        self.assertEqual(self.solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]), 6)


if __name__ == "__main__":
    unittest.main()
