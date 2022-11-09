class StockSpanner:

    def __init__(self):
        self.stack  = []        

    def next(self, price: int) -> int:
        s = 0
        while self.stack and price >= self.stack[-1][0]:
            s += self.stack.pop()[1]
        s += 1
        self.stack.append((price,s))
        return self.stack[-1][1]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)