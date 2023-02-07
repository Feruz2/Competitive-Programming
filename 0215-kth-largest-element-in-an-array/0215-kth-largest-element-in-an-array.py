class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for i in range(len(nums)):
            if k == len(heap):
                heappushpop(heap,(nums[i]))
            else:
                heappush(heap,(nums[i]))
        return heappop(heap)   
       