class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1
        num = nums[0]
        for i in range(len(nums)):
            if num < nums[i]:
                nums[pointer] = nums[i]
                pointer += 1
                num = nums[i]
        return pointer