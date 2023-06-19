class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        for i in range(3):
            res = res + word1[0]
            word1 = word1[1:]
            res = res + word2[0]
            word2 = word2[1:]
        return res


ress = Solution().mergeAlternately('abc', 'pqr')
print(ress)