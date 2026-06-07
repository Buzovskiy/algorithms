import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.455_assign_cookies.algorithm")
Solution = algorithm.Solution

class TestAssignCookies(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: g = [1,2,3], s = [1,1], Output: 1
        self.assertEqual(self.solution.findContentChildren([1, 2, 3], [1, 1]), 1)

    def test_example2(self):
        # Example 2: g = [1,2], s = [1,2,3], Output: 2
        self.assertEqual(self.solution.findContentChildren([1, 2], [1, 2, 3]), 2)

    def test_all_satisfied(self):
        self.assertEqual(self.solution.findContentChildren([1, 1], [1, 2]), 2)

    def test_none_satisfied(self):
        self.assertEqual(self.solution.findContentChildren([5, 6], [1, 2]), 0)

    def test_empty_cookies(self):
        self.assertEqual(self.solution.findContentChildren([1, 2], []), 0)

    def test_empty_children(self):
        self.assertEqual(self.solution.findContentChildren([], [1, 2]), 0)

    def test_large_cookies(self):
        self.assertEqual(self.solution.findContentChildren([10, 20], [30, 40]), 2)

if __name__ == "__main__":
    unittest.main()
