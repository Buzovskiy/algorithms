from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        output = []

        for word in words:
            letters = set(word.lower())
            if any(letters <= row for row in rows):
                output.append(word)

        return output
