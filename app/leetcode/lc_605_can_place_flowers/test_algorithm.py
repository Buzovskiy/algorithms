import unittest
from app.leetcode.lc_605_can_place_flowers.algorithm import Solution

class TestAlgorithm(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        self.assertTrue(self.solution.canPlaceFlowers(flowerbed, n))

    def test_example_2(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        self.assertFalse(self.solution.canPlaceFlowers(flowerbed, n))

    def test_single_zero_n1(self):
        flowerbed = [0]
        n = 1
        self.assertTrue(self.solution.canPlaceFlowers(flowerbed, n))

    def test_single_one_n1(self):
        flowerbed = [1]
        n = 1
        self.assertFalse(self.solution.canPlaceFlowers(flowerbed, n))

    def test_all_zeros_3_n2(self):
        flowerbed = [0, 0, 0]
        n = 2
        self.assertTrue(self.solution.canPlaceFlowers(flowerbed, n))

if __name__ == '__main__':
    unittest.main()
