class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(nums) -1
        dicit = defaultdict(list)
        for idx,val in enumerate(nums):
            dicit[val].append(idx)
    
        nums.sort()
        while l <= r:
            if nums[l]+nums[r] > target:
                r -= 1
            elif nums[l]+nums[r] < target:
                l += 1
            else:
                break
        if nums[l] != nums[r]:
            return [dicit[nums[l]][0],dicit[nums[r]][0]]
        else:
            return [dicit[nums[l]][0],dicit[nums[r]][1]]
        
        