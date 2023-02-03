class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        n = random.randint(1, self.w[-1])
        lo, hi = 0, len(self.w) - 1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if self.w[mid] == n:
                return mid
            if self.w[mid] < n:
                lo = mid + 1
            else:
                hi = mid
        return hi

    # Your Solution object will be instantiated and called as such:
    # obj = Solution(w)
    # param_1 = obj.pickIndex()