class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = []
        for val in nums:
            heappush(heap,val)
        cnt = 0
        soFar = 0
        while heap:
            val = heappop(heap)
            if val - soFar <= 0:
                continue
            else:
                cnt += 1
                soFar += (val - soFar)
        return cnt