import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_717_1_bit_and_2_bit_characters.algorithm")
Solution = algorithm.Solution


class TestOneBitAndTwoBitCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.isOneBitCharacter([1, 0, 0]))

    def test_example2(self):
        self.assertFalse(self.solution.isOneBitCharacter([1, 1, 1, 0]))

    def test_single_zero(self):
        self.assertTrue(self.solution.isOneBitCharacter([0]))

    def test_two_bit_before_last_zero(self):
        self.assertTrue(self.solution.isOneBitCharacter([1, 1, 0]))


if __name__ == "__main__":
    unittest.main()
