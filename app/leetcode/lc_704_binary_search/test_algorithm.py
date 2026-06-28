import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_704_binary_search.algorithm")
Solution = algorithm.Solution


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_example2(self):
        self.assertEqual(self.solution.search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_first_element(self):
        self.assertEqual(self.solution.search([1, 3, 5, 7], 1), 0)

    def test_last_element(self):
        self.assertEqual(self.solution.search([1, 3, 5, 7], 7), 3)

    def test_single_element_found(self):
        self.assertEqual(self.solution.search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(self.solution.search([5], -5), -1)


if __name__ == "__main__":
    unittest.main()
