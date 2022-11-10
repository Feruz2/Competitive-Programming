class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        left = [-1] * len(arr)
        right = [len(arr)] * len(arr)
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
            # print((i - left[i]),(right[i] - i))
            ans = ((i - left[i]) * (right[i] - i))*arr[i]
            total += ans
        return total % MOD