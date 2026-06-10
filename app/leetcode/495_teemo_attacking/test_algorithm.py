import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.495_teemo_attacking.algorithm")
Solution = algorithm.Solution

class TestTeemoAttacking(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: timeSeries = [1,4], duration = 2, Output: 4
        self.assertEqual(self.solution.findPoisonedDuration([1, 4], 2), 4)

    def test_example2(self):
        # Example 2: timeSeries = [1,2], duration = 2, Output: 3
        self.assertEqual(self.solution.findPoisonedDuration([1, 2], 2), 3)

    def test_empty_time_series(self):
        self.assertEqual(self.solution.findPoisonedDuration([], 2), 0)

    def test_single_attack(self):
        self.assertEqual(self.solution.findPoisonedDuration([1], 5), 5)

    def test_overlapping_attacks(self):
        # [1, 2, 3], duration 5
        # 1: 1-6 (ends at 6)
        # 2: 2-7 (ends at 7)
        # 3: 3-8 (ends at 8)
        # Total: [1, 8] -> 7 seconds? No, duration is inclusive [t, t + duration - 1]
        # 1: [1, 5], 2: [2, 6], 3: [3, 7]. Union: [1, 7] -> 7 seconds.
        # Calculation:
        # i=0: min(5, 2-1) = 1
        # i=1: min(5, 3-2) = 1
        # last: 5
        # Total: 1 + 1 + 5 = 7.
        self.assertEqual(self.solution.findPoisonedDuration([1, 2, 3], 5), 7)

    def test_no_overlap(self):
        # [1, 10, 20], duration 5
        # i=0: min(5, 10-1) = 5
        # i=1: min(5, 20-10) = 5
        # last: 5
        # Total: 15
        self.assertEqual(self.solution.findPoisonedDuration([1, 10, 20], 5), 15)

if __name__ == "__main__":
    unittest.main()
