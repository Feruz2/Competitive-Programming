class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        qu = deque()
        for i in range(k):
            while qu and nums[qu[-1]] < nums[i]:
                qu.pop()
            qu.append(i)
        ans = [nums[qu[0]]]
        for i in range(k,len(nums)):
            while qu and nums[qu[-1]] < nums[i]:
                qu.pop()
            qu.append(i)
            if i - k >= qu[0]:
                qu.popleft()
            ans.append(nums[qu[0]])
        return ans