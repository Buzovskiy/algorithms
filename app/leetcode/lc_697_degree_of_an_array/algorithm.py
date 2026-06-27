from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degrees = {}
        max_degree = 0
        num_set = set()
        indixes = {}
        for i, num in enumerate(nums):
            degrees[num] = degrees.get(num, 0) + 1
            if num not in indixes:
                indixes[num] = [i]

            if degrees[num] >= max_degree:
                indixes[num].append(i)

            if degrees[num] > max_degree:
                max_degree = degrees[num]
                num_set = set()
                num_set.add(num)
            elif degrees[num] == max_degree:
                num_set.add(num)

        #print(indixes)
        indexes_length = []
        for num in num_set:
            min_ind = indixes[num][0]
            max_ind = indixes[num][-1]
            indexes_length.append(max_ind+1-min_ind)
        return min(indexes_length)
