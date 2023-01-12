class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for val in nums:
            heappush(heap,-val)
        score = 0
        while k and heap:
            val = heappop(heap) * -1
            score += val
            nextt = ceil(val/3)
            heappush(heap,-nextt)
            k -= 1
        return score