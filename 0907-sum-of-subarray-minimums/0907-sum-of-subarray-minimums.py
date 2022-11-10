class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        left = [-1] * len(arr)
        right = [-1] * len(arr)
        s = []
        for i in range(len(arr)):
            while s and arr[s[-1]] >= arr[i]:
                right[s.pop()] = i
            s.append(i)
        s = []
        for i in range(len(arr) -1,-1,-1):
            while s and arr[s[-1]] > arr[i]:
                left[s.pop()] = i
            s.append(i)
        total = 0
        # print(left, right)
        for i in range(len(arr)):
            if left[i] == -1:
                l = i
                
            else:
                l = i - (left[i] + 1)
                
            if right[i] == -1:
                r = len(arr) - 1 - i
                
            else:
                r = (right[i] - 1) - i
            # print(l+1,r+1)
            r =  r + 1
            l = l + 1
            ans = (l * r)*arr[i]
            total += ans
        return total%MOD