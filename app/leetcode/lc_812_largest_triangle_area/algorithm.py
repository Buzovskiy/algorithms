from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        s_max = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if points[i] == points[j]:
                    continue
                for k in range(len(points)):
                    if points[i] == points[k] or points[j] == points[k]:
                        continue
                    x1 = points[i][0]
                    x2 = points[j][0]
                    x3 = points[k][0]
                    y1 = points[i][1]
                    y2 = points[j][1]
                    y3 = points[k][1]
                    s = 0.5*(abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
                    s_max = max(s_max, s)
        return s_max
