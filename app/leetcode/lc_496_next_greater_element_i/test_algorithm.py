import unittest

# Standard import works now as the package name starts with a letter
from app.leetcode.lc_496_next_greater_element_i.algorithm import Solution

class TestNextGreaterElementI(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: nums1 = [4,1,2], nums2 = [1,3,4,2]
        # Output: [-1,3,-1]
        self.assertEqual(self.solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])

    def test_example2(self):
        # Example 2: nums1 = [2,4], nums2 = [1,2,3,4]
        # Output: [3,-1]
        self.assertEqual(self.solution.nextGreaterElement([2, 4], [1, 2, 3, 4]), [3, -1])

    def test_no_next_greater(self):
        self.assertEqual(self.solution.nextGreaterElement([1, 2, 3], [3, 2, 1]), [-1, -1, -1])

    def test_all_greater(self):
        self.assertEqual(self.solution.nextGreaterElement([1, 2, 3], [1, 2, 3, 4]), [2, 3, 4])

if __name__ == "__main__":
    unittest.main()
