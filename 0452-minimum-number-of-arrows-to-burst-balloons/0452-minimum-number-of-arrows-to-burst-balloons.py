class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        point = sorted(points,key = lambda x: (x[0], x[1]))
        s = float('-inf')
        e = float('inf')
        arrow = 0
        for x_s, x_e in point:
            if s <= x_s <= e:
                s = max(s,x_s)
                e = min(e,x_e)
            else:
                arrow += 1
                s = x_s
                e = x_e
        return arrow + 1