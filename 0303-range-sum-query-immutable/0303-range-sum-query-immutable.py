class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix =[]
        sum_till = 0
        for value in nums:
            sum_till += value
            self.prefix.append(sum_till)
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right]-self.prefix[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)