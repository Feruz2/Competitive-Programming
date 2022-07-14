class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            real = nums[i] - 1
            if 0 <= real < len(nums) and nums[real] != nums[i]:
                nums[real],nums[i] = nums[i],nums[real]
            else:
                i += 1
        # print(nums)
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
            
        return len(nums)+1