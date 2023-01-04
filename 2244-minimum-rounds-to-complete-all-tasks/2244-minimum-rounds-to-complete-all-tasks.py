class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        c=Counter(tasks)
        res=0
        for i,n in c.items():
            if n<2:
                return -1
            res+=math.ceil(n/3)
        return res