import importlib
import unittest


algorithm = importlib.import_module(
    "app.leetcode.lc_744_find_smallest_letter_greater_than_target.algorithm"
)
Solution = algorithm.Solution


class TestFindSmallestLetterGreaterThanTarget(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.nextGreatestLetter(["c", "f", "j"], "a"), "c")

    def test_example2(self):
        self.assertEqual(self.solution.nextGreatestLetter(["c", "f", "j"], "c"), "f")

    def test_example3(self):
        self.assertEqual(self.solution.nextGreatestLetter(["x", "x", "y", "y"], "z"), "x")

    def test_target_before_first_duplicate_group(self):
        self.assertEqual(self.solution.nextGreatestLetter(["c", "f", "f", "j"], "e"), "f")

    def test_target_equal_to_duplicate_group(self):
        self.assertEqual(self.solution.nextGreatestLetter(["c", "f", "f", "j"], "f"), "j")


if __name__ == "__main__":
    unittest.main()
