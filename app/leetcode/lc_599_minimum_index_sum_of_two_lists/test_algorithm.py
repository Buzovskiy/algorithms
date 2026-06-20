import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_599_minimum_index_sum_of_two_lists.algorithm")
Solution = algorithm.Solution

class TestMinimumIndexSumOfTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
        # Order doesn't matter according to description, but here it's single element
        self.assertEqual(self.solution.findRestaurant(list1, list2), ["Shogun"])

    def test_example2(self):
        list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["KFC","Shogun","Burger King"]
        self.assertEqual(self.solution.findRestaurant(list1, list2), ["Shogun"])

    def test_example3(self):
        list1 = ["happy","sad","good"]
        list2 = ["sad","happy","good"]
        result = self.solution.findRestaurant(list1, list2)
        self.assertCountEqual(result, ["sad","happy"])

if __name__ == "__main__":
    unittest.main()
