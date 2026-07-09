from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_plate_counts = {}
        licensePlate = licensePlate.lower()
        for l in licensePlate:
            if l.isalpha():
                license_plate_counts[l] = license_plate_counts.get(l, 0) + 1
        words_counts = []
        for word in words:
            counts = {}
            word = word.lower()
            for l in word:
                counts[l] = counts.get(l, 0) + 1
            words_counts.append(counts)
        min_word = None

        for i, word in enumerate(words_counts):
            all_letters_exist = True
            for k, v in license_plate_counts.items():
                if k not in word:
                    all_letters_exist = False
                    continue
                if v > word[k]:
                    all_letters_exist = False
            if all_letters_exist:
                if min_word is None or len(min_word) > len(words[i]):
                    min_word = words[i]
        
        return min_word
