import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_905_sort_array_by_parity.algorithm")
Solution = algorithm.Solution


class TestSortArrayByParity(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assert_valid_parity_sort(self, nums, result):
        self.assertCountEqual(result, nums)

        seen_odd = False
        for number in result:
            if number % 2 == 1:
                seen_odd = True
            elif seen_odd:
                self.fail("Even number appears after an odd number")

    def test_example1(self):
        nums = [3, 1, 2, 4]

        result = self.solution.sortArrayByParity(nums)

        self.assert_valid_parity_sort([3, 1, 2, 4], result)

    def test_example2(self):
        self.assertEqual(self.solution.sortArrayByParity([0]), [0])

    def test_all_even(self):
        nums = [2, 4, 6]

        result = self.solution.sortArrayByParity(nums)

        self.assert_valid_parity_sort([2, 4, 6], result)

    def test_all_odd(self):
        nums = [1, 3, 5]

        result = self.solution.sortArrayByParity(nums)

        self.assert_valid_parity_sort([1, 3, 5], result)


if __name__ == "__main__":
    unittest.main()
