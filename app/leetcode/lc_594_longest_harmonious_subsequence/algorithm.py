from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_seq = 0
        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        for num in nums_dict:
            if num + 1 in nums_dict:
                max_seq = max(max_seq, nums_dict[num] + nums_dict[num + 1])

        return max_seq
