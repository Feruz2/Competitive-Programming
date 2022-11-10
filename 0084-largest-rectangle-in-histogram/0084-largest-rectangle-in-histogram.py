class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        left = [-1]*len(heights)
        right = [len(heights)] * len(heights)
        for i in range(len(heights)):
            while s and heights[s[-1]]> heights[i]:
                right[s.pop()] = i
            s.append(i)
        s = []
        for i in range(len(heights)-1,-1,-1):
            while s and heights[s[-1]] > heights[i]:
                left[s.pop()] = i
            s.append(i)
        ans = 0
        # print(left,right)
        for i in range(len(heights)):
            ans = max(ans,(right[i] - left[i] - 1) * heights[i])
        return ans