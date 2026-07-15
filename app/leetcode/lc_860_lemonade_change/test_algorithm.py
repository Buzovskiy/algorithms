import unittest

from app.leetcode.lc_860_lemonade_change.algorithm import Solution


class TestLemonadeChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.lemonadeChange([5, 5, 5, 10, 20]))

    def test_example2(self):
        self.assertFalse(self.solution.lemonadeChange([5, 5, 10, 10, 20]))

    def test_first_customer_pays_ten(self):
        self.assertFalse(self.solution.lemonadeChange([10]))

    def test_can_use_three_fives_for_twenty(self):
        self.assertTrue(self.solution.lemonadeChange([5, 5, 5, 20]))


if __name__ == "__main__":
    unittest.main()
