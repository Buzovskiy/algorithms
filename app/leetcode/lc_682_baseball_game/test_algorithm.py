import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_682_baseball_game.algorithm")
Solution = algorithm.Solution


class TestBaseballGame(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.calPoints(["5", "2", "C", "D", "+"]), 30)

    def test_example2(self):
        self.assertEqual(self.solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)

    def test_example3(self):
        self.assertEqual(self.solution.calPoints(["1", "C"]), 0)


if __name__ == "__main__":
    unittest.main()
