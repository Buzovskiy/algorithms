from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        current_number = 0
        flag = False
        for num in nums:
            if num == 1:
                current_number += 1
                flag = True
            elif num == 0 and flag == True:
                flag = False
                if current_number > output:
                    output = current_number
                current_number = 0
        if current_number > output:
            output = current_number
        return output
