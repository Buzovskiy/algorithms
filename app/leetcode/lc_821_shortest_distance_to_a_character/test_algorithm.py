import importlib
import unittest


algorithm = importlib.import_module(
    "app.leetcode.lc_821_shortest_distance_to_a_character.algorithm"
)
Solution = algorithm.Solution


class TestShortestDistanceToACharacter(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(
            self.solution.shortestToChar("loveleetcode", "e"),
            [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0],
        )

    def test_example2(self):
        self.assertEqual(
            self.solution.shortestToChar("aaab", "b"),
            [3, 2, 1, 0],
        )

    def test_character_at_start(self):
        self.assertEqual(
            self.solution.shortestToChar("baaa", "b"),
            [0, 1, 2, 3],
        )

    def test_multiple_occurrences(self):
        self.assertEqual(
            self.solution.shortestToChar("abacada", "a"),
            [0, 1, 0, 1, 0, 1, 0],
        )


if __name__ == "__main__":
    unittest.main()
