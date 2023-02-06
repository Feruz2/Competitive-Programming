class DetectSquares:

    def __init__(self):
        self.counter = Counter()
        

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for x1, y1 in self.counter.keys():
            if abs(x -x1) == abs(y - y1) and abs(x -x1):
                res += self.counter[(x1,y1)]* self.counter[(x1,y)]*self.counter[(x,y1)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)