class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @cache
        def rec(idx1,ch,di):
            if idx1 == len(nums):
                return 0
            one = 0
            if nums[idx1] > ch and di == "U":
                one  =  1 + rec(idx1+1,nums[idx1],"L")
            elif nums[idx1] < ch and di == "L":
                one =  1 + rec(idx1+1,nums[idx1],"U")
            return max(rec(idx1+1,ch,di),one)
        num1 = [-1] + nums
        nums = [10001] + nums
        return max(rec(1,num1[0],"U"),rec(1,nums[0],"L"))