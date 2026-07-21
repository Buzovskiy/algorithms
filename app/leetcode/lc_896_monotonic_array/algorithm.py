from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decreasing = False
        increasing = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increasing = True
                if decreasing == True:
                    return False
            elif nums[i] == nums[i-1]:
                continue
            else:
                decreasing = True
                if increasing == True:
                    return False
        return True
