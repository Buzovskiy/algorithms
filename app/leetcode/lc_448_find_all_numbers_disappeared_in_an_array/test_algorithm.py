import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_448_find_all_numbers_disappeared_in_an_array.algorithm")
Solution = algorithm.Solution

class TestFindDisappearedNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: nums = [4,3,2,7,8,2,3,1], Output: [5,6]
        nums = [4,3,2,7,8,2,3,1]
        self.assertEqual(self.solution.findDisappearedNumbers(nums), [5, 6])

    def test_example2(self):
        # Example 2: nums = [1,1], Output: [2]
        nums = [1,1]
        self.assertEqual(self.solution.findDisappearedNumbers(nums), [2])

    def test_no_disappeared(self):
        # nums = [1, 2, 3], Output: []
        nums = [1, 2, 3]
        self.assertEqual(self.solution.findDisappearedNumbers(nums), [])

    def test_all_disappeared(self):
        # nums = [1, 1, 1], Output: [2, 3]
        nums = [1, 1, 1]
        self.assertEqual(self.solution.findDisappearedNumbers(nums), [2, 3])

    def test_single_element_present(self):
        nums = [1]
        self.assertEqual(self.solution.findDisappearedNumbers(nums), [])

    def test_single_element_missing(self):
        # This case is not possible given constraints n == nums.length and 1 <= nums[i] <= n
        # But if nums = [2] and n=1 it would be out of bounds.
        # However, for n=2, nums=[1, 1], output is [2] (already covered)
        pass

if __name__ == "__main__":
    unittest.main()
