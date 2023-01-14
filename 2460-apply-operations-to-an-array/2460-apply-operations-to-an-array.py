class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1 ):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        r = 0
        i = 0
        # print(nums)
        while i < len(nums):
            if nums[i] == 0:
                r = i
                while r < len(nums) and nums[r] == 0:
                    r += 1
                if r == len(nums): break
                nums[i], nums[r] = nums[r], nums[i]
            i+=1
        return nums
            
                