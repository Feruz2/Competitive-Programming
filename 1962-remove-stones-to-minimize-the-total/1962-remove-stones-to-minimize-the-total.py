class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in range(len(piles)):
            heappush(heap,-piles[i])
        while heap and k:
            x = heappop(heap)
            heappush(heap,x//2)
            k -= 1
        s = 0
        for val in heap:
            s += (-1*val)
        return s