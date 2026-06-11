from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_duration = 0
        for i in range(len(timeSeries) - 1):
            # The duration between two attacks is either the full duration 
            # or the gap between them if the second attack happens before 
            # the first one's effect ends.
            total_duration += min(duration, timeSeries[i+1] - timeSeries[i])
            
        # The last attack always adds the full duration.
        total_duration += duration
        return total_duration
