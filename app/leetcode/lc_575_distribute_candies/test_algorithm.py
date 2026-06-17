import unittest
from app.leetcode.lc_575_distribute_candies.algorithm import Solution

class TestAlgorithm(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        candyType = [1, 1, 2, 2, 3, 3]
        expected = 3
        self.assertEqual(self.solution.distributeCandies(candyType), expected)

    def test_example2(self):
        candyType = [1, 1, 2, 3]
        expected = 2
        self.assertEqual(self.solution.distributeCandies(candyType), expected)

    def test_example3(self):
        candyType = [6, 6, 6, 6]
        expected = 1
        self.assertEqual(self.solution.distributeCandies(candyType), expected)

if __name__ == '__main__':
    unittest.main()
