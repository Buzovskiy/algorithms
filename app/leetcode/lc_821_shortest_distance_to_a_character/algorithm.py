from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        output = [0 for i in range(len(s))]
        left_to_right = []
        current_ind = None
        for i, l in enumerate(s):
            if l == c:
                current_ind = i
            left_to_right.append(None if current_ind is None else abs(current_ind-i))
        
        right_to_left = [0 for i in range(len(s))]
        for i in range(len(s)):
            i = len(s)-1-i
            if s[i] == c:
                current_ind = i
            right_to_left[i] = None if current_ind is None else abs(current_ind-i)
            if right_to_left[i] is None:
                output[i] = left_to_right[i]
            elif left_to_right[i] is None:
                output[i] = right_to_left[i]
            else:
                output[i] = min(right_to_left[i], left_to_right[i])
            
        return output
