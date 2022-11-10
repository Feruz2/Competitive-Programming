class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        left = 0
        nums.append(float('-inf'))
        s = [-1]
        for i in range(len(nums)):
            while nums[s[-1]] > nums[i]:
                print(i)
                mid = s.pop()
                interval = ((mid - s[-1]) * (i-mid)) * nums[mid]
                left += interval
            s.append(i)
        nums.pop()
        right = 0
        nums.append(float('inf'))
        s = [-1]
        for i in range(len(nums)):
            while nums[s[-1]] < nums[i]:
                mid = s.pop()
                interval = ((mid - s[-1]) * (i-mid)) * nums[mid]
                right += interval
            s.append(i)
            
        return right - left
        