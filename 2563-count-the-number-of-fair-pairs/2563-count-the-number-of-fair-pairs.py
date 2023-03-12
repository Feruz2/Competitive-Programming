class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def search(value):
            l = 0
            r = len(nums) - 1
            best = -1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] > value:
                    r = mid  - 1
                elif nums[mid] <= value:
                    best = mid
                    l = mid + 1
            return best
                    
        
        
        nums.sort()
        print(nums)
        ans = 0
        for idx,num in enumerate(nums):
            val = lower - num
            left = bisect_left(nums,val,idx+1)
            val = upper - num
            right = bisect_right(nums,val,idx+1)
            
            ans += right-left
        return ans
                