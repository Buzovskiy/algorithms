import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.350_intersection_of_two_arrays_ii.algorithm")
Solution = algorithm.Solution


class TestIntersect(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intersect_example1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        result = self.solution.intersect(nums1, nums2)
        self.assertCountEqual(result, [2, 2])

    def test_intersect_example2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        result = self.solution.intersect(nums1, nums2)
        # Expected intersection: one 4, one 9
        self.assertCountEqual(result, [4, 9])

    def test_intersect_no_common(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [])

    def test_intersect_empty_input(self):
        self.assertEqual(self.solution.intersect([], [1]), [])
        self.assertEqual(self.solution.intersect([1], []), [])
        self.assertEqual(self.solution.intersect([], []), [])

    def test_intersect_all_common(self):
        nums1 = [1, 1, 1]
        nums2 = [1, 1]
        result = self.solution.intersect(nums1, nums2)
        self.assertCountEqual(result, [1, 1])


if __name__ == "__main__":
    unittest.main()
