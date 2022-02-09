import unittest
from app.leetcode.palindrome_number import Solution


class TestPalindromeNumber(unittest.TestCase):
    def test_palindrome_number(self):
        self.assertTrue(Solution().isPalindrome(121))
        self.assertFalse(Solution().isPalindrome(-121))
        self.assertFalse(Solution().isPalindrome(10))
