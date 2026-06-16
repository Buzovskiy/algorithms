from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = {}

        for i, s in enumerate(sorted(score, reverse=True)):
            rank[s] = medals[i] if i < 3 else str(i + 1)

        return [rank[s] for s in score]
