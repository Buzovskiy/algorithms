from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        pair = []
        nums.sort()
        sum = 0
        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum
