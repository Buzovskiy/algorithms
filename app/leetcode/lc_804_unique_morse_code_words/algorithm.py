from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letter_morse_map = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                            "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                            "--.."]
        morse_words = []
        for word in words:
            morse_word = ""
            for letter in word:
                index = ord(letter) - ord("a")
                morse_word += letter_morse_map[index]
            morse_words.append(morse_word)
        return len(set(morse_words))
