class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum_ = 0        
        for i in range(len(nums)):
            min_ = float('inf')
            max_ = float('-inf')
            for j in range(i,len(nums)):
                min_ = min(min_,nums[j])
                max_ = max(max_ , nums[j])
                sum_ += max_ - min_
        return sum_