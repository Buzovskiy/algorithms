import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_748_shortest_completing_word.algorithm")
Solution = algorithm.Solution


class TestShortestCompletingWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(
            self.solution.shortestCompletingWord(
                "1s3 PSt",
                ["step", "steps", "stripe", "stepple"],
            ),
            "steps",
        )

    def test_example2(self):
        self.assertEqual(
            self.solution.shortestCompletingWord(
                "1s3 456",
                ["looks", "pest", "stew", "show"],
            ),
            "pest",
        )

    def test_repeated_letters(self):
        self.assertEqual(
            self.solution.shortestCompletingWord(
                "aBc 12c",
                ["abccdef", "caaacab", "cbca"],
            ),
            "cbca",
        )

    def test_returns_first_shortest(self):
        self.assertEqual(
            self.solution.shortestCompletingWord(
                "GrC8950",
                ["measure", "other", "every", "base", "according", "level", "meeting"],
            ),
            "according",
        )


if __name__ == "__main__":
    unittest.main()
