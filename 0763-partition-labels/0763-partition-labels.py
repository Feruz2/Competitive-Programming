class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        h = defaultdict(int)
        for i in range(len(s)):
            h[s[i]]  = i
        left = 0
        right = 0

        while left < len(s):
            right = max(right, h[s[left]])
            temp = left
            while temp < right:
                temp += 1
                right = max(right, h[s[temp]])
            ans.append(right - left + 1)
            left = right + 1
        return ans
