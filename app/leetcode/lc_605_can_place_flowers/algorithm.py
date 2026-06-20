from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        output = 0
        prev = None
        for i in range(0, len(flowerbed)):
            if prev is None and flowerbed[i] == 0:
                output += 1
                prev = 1
            elif prev is None and flowerbed[i] == 1:
                prev = 1
            elif flowerbed[i] == 1 and prev == 1:
                output -= 1
            elif flowerbed[i] == 0 and prev == 1:
                prev = 0
            elif flowerbed[i] == 0 and prev == 0:
                output += 1
                prev = 1
            elif flowerbed[i] == 1 and prev == 0:
                prev = 1

        if output >= n:
            return True
        return False
