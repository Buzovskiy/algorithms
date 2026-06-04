from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        output = []
        for num in nums1:
            nums1_dict[num] = nums1_dict.get(num, 0) + 1
        for num in nums2:
            if num in nums1_dict and nums1_dict[num] > 0:
                output.append(num)
                nums1_dict[num] = nums1_dict[num] - 1
        return output
