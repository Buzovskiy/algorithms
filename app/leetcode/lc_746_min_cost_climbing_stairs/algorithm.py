from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost))]
        for i in range(len(cost)):
            ii = len(cost) - 1 - i
            #print(ii)
            if ii == len(cost) - 1:
                dp[ii] = cost[-1]
            elif ii == len(cost) - 2:
                dp[ii] = cost[-2]
            else:
                dp[ii] = cost[ii] + min(dp[ii+1], dp[ii+2])
        
        return min(dp[0], dp[1])
