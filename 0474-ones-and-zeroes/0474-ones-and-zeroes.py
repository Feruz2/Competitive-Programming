class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = []
        for i in range(len(strs)):
            z,o = 0,0
            for j in range(len(strs[i])):
                if strs[i][j] == '1':
                    o += 1
                else:
                    z += 1
            arr.append((z,o))
    
        dp = defaultdict(int)
        @cache
        def rec(z,o,idx):
            if z > m or o > n:
                return 0 
            if idx >= len(arr):
                if z <= m and o<=n:
                    return 1
                return 0
            one = 1 + rec(z + arr[idx][0], o + arr[idx][1], idx + 1)
            two = rec(z, o, idx + 1)
            return max(one,two)
       
        return  rec(0,0,0) - 1
                           
                           
        