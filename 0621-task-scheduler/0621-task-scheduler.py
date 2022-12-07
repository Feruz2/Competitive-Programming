class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        dicit = defaultdict(int)
        for i in range(len(tasks)):
            dicit[tasks[i]] += 1
        lst = sorted(dicit.items(), key = lambda x:x[1])
        # print(lst)
        ans = (lst[-1][1] - 1)*n
        s = -1
        # print(ans)
        x = ans// n
        for i in range(len(lst) - 2 ,-1 ,-1):
            if lst[i][1] == lst[i+1][1]:
                ans -= x
                # print(ans)
            else:
                s = i
                break
        # print(ans)         
        for i in range(s,-1,-1):
            
            ans -= lst[i][1]
            
            
        return max(ans,0) + len(tasks)
            