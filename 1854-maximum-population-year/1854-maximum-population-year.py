class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        lst = [0] * 1002
        for birth, death in logs:
            lst[birth-1950] += 1
            lst[death - 1950] -= 1
        s = 0
        for i in range(len(lst)):
            s += lst[i]
            lst[i] = s
        maxx = max(lst)
        for i in range(len(lst)):
            if lst[i] == maxx:
                return i + 1950
        return -1