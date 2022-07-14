class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dicit = defaultdict(int)
        for head,tail in edges:
            dicit[tail] += 1
        ans = []
        for i in range(n):
            if i not in dicit:
                ans.append(i)
        return ans