class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        z = 1
        odd = False
        if n%2 != 0:
            n -= 1
            odd = True
        for i in range(n//2):
            ans.append(z)
            ans.append(-z)
            z += 1
        if odd:
            ans.append(0)
        return ans
            
            