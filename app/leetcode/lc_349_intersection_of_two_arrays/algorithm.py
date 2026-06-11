from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        for num in nums1:
            nums1_dict[num] = 0
        result = set()
        for num in nums2:
            if num in nums1_dict:
                result.add(num)
        return list(result)