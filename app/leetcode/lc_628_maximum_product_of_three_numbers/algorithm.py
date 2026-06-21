from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        output = 1
        nums.sort()
        last_index = len(nums) - 1
        first_triplet =  nums[last_index]*nums[last_index-1]*nums[last_index-2]
        second_triplet = nums[0]*nums[1]*nums[last_index]

        return max(first_triplet, second_triplet)
