class Solution:

    @classmethod
    def twoSum(cls, nums: list, target: int) -> list:
        for i1, el1 in enumerate(nums):
            for i2, el2 in enumerate(nums):
                if i1 != i2 and el1 + el2 == target:
                    return [i1, i2]

    @classmethod
    def two_sum_enhanced(cls, nums: list, target: int) -> list:
        for i in range(len(nums)):
            el2 = target - nums[i]
            el2_inds = [i2 for i2, _el2 in enumerate(nums) if _el2 == el2 and i2 != i]
            if len(el2_inds):
                return [i, el2_inds[0]]

    @classmethod
    def two_sum_best(cls, nums: list, target: int) -> list:
        element_maps = {}
        for i in range(len(nums)):
            if nums[i] in element_maps:
                return [element_maps[nums[i]], i]
            else:
                element_maps[target - nums[i]] = i
