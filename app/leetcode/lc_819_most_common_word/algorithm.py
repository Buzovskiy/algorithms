from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for symbol in "!?',;.":
            paragraph = paragraph.replace(symbol, " ")
 
        words_count = {}
        max_count = 0
        for word in paragraph.lower().split():
            words_count[word] = words_count.get(word, 0) + 1
            if max_count < words_count[word] and word not in banned and word:
                max_count = words_count[word]
                max_word = word
        return max_word
