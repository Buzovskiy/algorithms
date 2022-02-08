class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i1, el1 in enumerate(nums):
            for i2, el2 in enumerate(nums):
                if i1 != i2 and el1 + el2 == target:
                    return [i1, i2]

