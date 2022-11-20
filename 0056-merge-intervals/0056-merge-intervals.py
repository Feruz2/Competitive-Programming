class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0],x[1]))
        new = []
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1,len(intervals)):
            
            if right >= intervals[i][0]:
                right = max(right,intervals[i][1])
                
            else:
                new.append([left,right])
                left = intervals[i][0]
                right = intervals[i][1]

        new.append([left,right])
        return new