class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        qu = deque([(amount,0)])
        level = 0
        done = defaultdict(int)
        while qu:
            N = len(qu)
            for i in range(N):
                num,time = qu.popleft()
                if num in done:
                    continue
                done[num] = 1
                if num == 0:
                    return time
                for val in coins:
                    x = num - val
                    if x >= 0:
                        qu.append((x,time+1))
        return -1