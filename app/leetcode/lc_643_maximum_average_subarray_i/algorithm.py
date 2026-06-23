from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        output = None
        for i in range(len(nums)-k+1):
            if i == 0:
                current_sum = 0
                for j in range(i, i+k):
                    current_sum += nums[j]
            else:
                current_sum = current_sum - nums[i-1] + nums[i+k-1]

            avr = current_sum / k
            if output is None or avr > output:
                output = avr
        return output
