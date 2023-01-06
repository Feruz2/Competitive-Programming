class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
       
        dicit = defaultdict(str)
        lst = s.split()
        s = lst
        done = set()
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            if s[i] not in dicit:
                if pattern[i] not in done:
                    dicit[s[i]] = pattern[i]
                    done.add(pattern[i])
                else:
                    return False
            elif dicit[s[i]] == pattern[i]:
                continue
            else:
                print(pattern[i],s[i],dicit[s[i]])
                return False
        return True