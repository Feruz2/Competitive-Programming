class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor = 0
        for i in range(1,n+1):
            xor^=i
        for val in nums:
            xor^=val
        point = -1
        for i in range(32):
            if xor&1<<i > 0:
                point = i
                break
        one,zero = 0,0
        for val in nums:
            if val&1<<point > 0:
                one ^= val
            else:
                zero ^= val
        for val in range(1,n+1):
            if val&1<<point > 0:
                one ^= val
            else:
                zero ^= val
        for val in nums:
            if val == one:
                return [one, zero]
        return [zero, one]
            