from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        output = 0
        current = 0
        last = None
        for num in nums:
            if last is None:
                current = 1
            elif num > last:
                current += 1
            else:
                current = 1
            last = num
            output = current if current > output else output
        return output
