class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    ans = nums[i] + nums[j]
                    if ans == target:
                        
                        cnt += 1
        return cnt