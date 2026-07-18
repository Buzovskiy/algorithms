from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        totalAlice = sum(aliceSizes)
        totalBob = sum(bobSizes)
        total = totalAlice + totalBob
        

        if totalAlice < totalBob:
            minSize = aliceSizes
            maxSize = bobSizes
            minTotal = totalAlice
            maxSizeHas = 'Bob'
        else:
            minSize = bobSizes
            minTotal = totalBob
            maxSize = aliceSizes
            maxSizeHas = 'Alice'

        for box in minSize:
            diff = total // 2 - (minTotal - box)
            if diff in maxSize:
                if maxSizeHas == 'Bob':
                    return [box, diff]
                else:
                    return [diff, box]
