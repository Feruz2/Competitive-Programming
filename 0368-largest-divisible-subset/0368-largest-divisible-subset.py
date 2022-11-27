class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        nums.sort()
        dicit = defaultdict(int)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] % nums[j] == 0:
                    if ans[i] < 1 + ans[j]:
                        ans[i] = 1 + ans[j]
                        dicit[nums[i]] = nums[j]
        can = max(ans)
        for i in range(len(ans)):
            if ans[i] == can:
                can = nums[i]
                break
        final = []
    
        while dicit[can] != 0:
            final.append(can)
            can = dicit[can]
        final.append(can)
        return final 