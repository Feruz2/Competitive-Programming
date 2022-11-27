class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lst = sorted(words, key = lambda x: (len(x),x))
        ans = [1] * len(words)
        for i in range(len(lst)):
            for j in range(0,i):
                if len(lst[i]) == len(lst[j]) + 1:
            
                    diff = 0
                    l = 0
                    r = 0
                    while l < len(lst[j]) and r < len(lst[i]):
                        if lst[i][r] != lst[j][l]:
                            diff += 1
                            r +=1
                            continue
                        l += 1
                        r += 1
                    diff += len(lst[i]) - r
                    diff += len(lst[j]) - l
                    if diff < 2:
                        ans[i] = max(ans[i],1 + ans[j])
                # print(ans)
        return max(ans)