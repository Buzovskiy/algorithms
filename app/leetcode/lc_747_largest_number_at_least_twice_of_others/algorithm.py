from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxInd = None
        maxNum = 0
        for i, num in enumerate(nums):
            if num > maxNum:
                maxNum = num
                maxInd = i
        maxSecondNum = 0
        for i, num in enumerate(nums):
            if num > maxSecondNum and num != maxNum:
                maxSecondNum = num
                if maxNum < 2 * maxSecondNum:
                    return -1
        return maxInd
