import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.intersection_of_two_arrays.algorithm")
Solution = algorithm.Solution


class TestIntersection(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intersection_example1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        result = self.solution.intersection(nums1, nums2)
        self.assertCountEqual(result, [2])

    def test_intersection_example2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        result = self.solution.intersection(nums1, nums2)
        self.assertCountEqual(result, [9, 4])

    def test_intersection_no_common(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(result, [])

    def test_intersection_empty_input(self):
        self.assertEqual(self.solution.intersection([], [1]), [])
        self.assertEqual(self.solution.intersection([1], []), [])
        self.assertEqual(self.solution.intersection([], []), [])

    def test_intersection_identical(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]
        result = self.solution.intersection(nums1, nums2)
        self.assertCountEqual(result, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
