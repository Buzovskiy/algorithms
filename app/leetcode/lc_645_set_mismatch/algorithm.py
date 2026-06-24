from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        output = []
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            if nums_dict[num] == 2:
                output.append(num)
        
        for i in range(1, len(nums)+1):
            if i not in nums_dict:
                output.append(i)
                return output
