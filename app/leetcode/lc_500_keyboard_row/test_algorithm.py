import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_500_keyboard_row.algorithm")
Solution = algorithm.Solution

class TestKeyboardRow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        words = ["Hello", "Alaska", "Dad", "Peace"]
        expected = ["Alaska", "Dad"]
        self.assertEqual(self.solution.findWords(words), expected)

    def test_example2(self):
        words = ["omk"]
        expected = []
        self.assertEqual(self.solution.findWords(words), expected)

    def test_example3(self):
        words = ["adsdf", "sfd"]
        expected = ["adsdf", "sfd"]
        self.assertEqual(self.solution.findWords(words), expected)

    def test_case_insensitivity(self):
        words = ["QwErTy", "AsDfGh", "ZxCvBn"]
        expected = ["QwErTy", "AsDfGh", "ZxCvBn"]
        self.assertEqual(self.solution.findWords(words), expected)

if __name__ == "__main__":
    unittest.main()
