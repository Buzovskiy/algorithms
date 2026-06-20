from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_sum = None
        list2_dict = {}
        output = []
        for i2, word2 in enumerate(list2):
            list2_dict[word2] = i2

        for i1, word1 in enumerate(list1):
            if word1 in list2_dict:
                indexes_sum = i1 + list2_dict[word1]
                if least_sum is None:
                    output.append(word1)
                    least_sum = indexes_sum
                elif indexes_sum == least_sum:
                    output.append(word1)
                elif indexes_sum < least_sum:
                    output = [word1]
                    least_sum = indexes_sum
        return output
