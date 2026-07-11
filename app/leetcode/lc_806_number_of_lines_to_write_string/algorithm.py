from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        current_width = 0
        line_number = 1
        for letter in s:
            letter_ind = ord(letter) - ord('a')
            if current_width + widths[letter_ind] <= 100:
                current_width += widths[letter_ind]
            else:
                current_width = widths[letter_ind]
                line_number += 1
        return [line_number, current_width]
