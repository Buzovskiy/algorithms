import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_819_most_common_word.algorithm")
Solution = algorithm.Solution


class TestMostCommonWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(
            self.solution.mostCommonWord(
                "Bob hit a ball, the hit BALL flew far after it was hit.",
                ["hit"],
            ),
            "ball",
        )

    def test_example2(self):
        self.assertEqual(self.solution.mostCommonWord("a.", []), "a")


if __name__ == "__main__":
    unittest.main()
