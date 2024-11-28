class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        line_start = [0] * len(nums)
        line_end = [0] * len(nums)
        for i in range(len(queries)):

            line_start[queries[i][0]] -= 1
            line_end[queries[i][1]] += 1
        total = 0
        for i in range(len(line_start)):
            
            if line_end[i] > 0:
                line_start[i] += total
                total = line_start[i] + line_end[i]
            else:
                total += line_start[i]
                line_start[i] = total
            
                 
        for i in range(len(nums)):
            if -line_start[i] < nums[i]:
                return False
        return True