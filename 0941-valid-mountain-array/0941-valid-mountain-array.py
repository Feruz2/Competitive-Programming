class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag = False
        for i in range(1,len(arr) - 1):
            if not flag and arr[i-1] < arr[i] > arr[i+1]:
                flag = True  
            elif not flag and not (arr[i-1] < arr[i] < arr[i+1]):
                return False
            elif flag and  not (arr[i-1] > arr[i] > arr[i+1]):
                return False
        return flag