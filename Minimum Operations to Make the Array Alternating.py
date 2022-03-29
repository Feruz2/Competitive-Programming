class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dicit1 ={}
        dicit2 ={}
        arr = nums
        for i in range(0,len(nums),2):
            if arr[i] not in dicit1:
                dicit1[arr[i]] = 1
            else:
                dicit1[arr[i]]+= 1
                
        for i in range(1,len(nums),2):
            if arr[i] not in dicit2:
                dicit2[arr[i]] = 1
            else:
                dicit2[arr[i]]+= 1
        sorted_dict1  = dict(sorted(dicit1.items(), key=lambda item: item[1],reverse=True))
        sorted_dict2 =  dict(sorted(dicit2.items(), key=lambda item: item[1],reverse=True))
        evenlist = list(sorted_dict1.values())
        oddlist = list(sorted_dict2.values())
        even = 0
        odd = 0
        if len(evenlist) > 0:
            even = evenlist[0]
        if len(oddlist) > 0:
            odd = oddlist[0]
        # print(even,odd,sorted_dict1,sorted_dict2)
        ans = 0
        if len(sorted_dict1) > 0 and len(sorted_dict2) > 0 and list(sorted_dict1.keys())[0] != list(sorted_dict2.keys())[0]:
            ans = len(nums) - even - odd
        elif len(sorted_dict1) > 0 and len(sorted_dict2) > 0:
            second_dicit1 = 0
            second_dicit2 = 0
            if len(dicit1) > 1:
                second_dicit1 = evenlist[1]
            if len(dicit2) >1:
                second_dicit2 = oddlist[1]
            ans = len(nums) - max(second_dicit1 + odd, even + second_dicit2)
        return ans
