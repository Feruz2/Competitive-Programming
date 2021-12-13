class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        digits=[]
        for num in nums:
            digits = [int(x) for x in str(num)]       
        digit.sort()
        digit.reverse(True)
        return[str(i) for i in digit]
        