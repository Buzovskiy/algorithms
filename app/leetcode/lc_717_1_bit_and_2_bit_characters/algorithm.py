from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        is_one_bit = False
        while i < len(bits):
            if bits[i] == 0:
                is_one_bit = True
                i += 1
            else:
                i = i + 2
                is_one_bit = False
        return is_one_bit
