import unittest

from app.leetcode.lc_747_largest_number_at_least_twice_of_others.algorithm import Solution


class TestLargestNumberAtLeastTwiceOfOthers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.dominantIndex([3, 6, 1, 0]), 1)

    def test_example2(self):
        self.assertEqual(self.solution.dominantIndex([1, 2, 3, 4]), -1)

    def test_two_numbers_dominant(self):
        self.assertEqual(self.solution.dominantIndex([0, 1]), 1)

    def test_largest_at_start(self):
        self.assertEqual(self.solution.dominantIndex([10, 2, 5, 1]), 0)

    def test_largest_not_twice_second_largest(self):
        self.assertEqual(self.solution.dominantIndex([2, 3, 4]), -1)


if __name__ == "__main__":
    unittest.main()
