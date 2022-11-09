class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        miss = 0
        for i in range(1,n+1):
            if i not in s:
                miss = i
                break
        s = set()
        for val in nums:
            if val in s:
                rep = val
                break
            s.add(val)
        return [rep,miss]
       