class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def fun(lst, summ, idx):
            # print(lst, summ, idx)
            if summ == target:
                ans.append(lst[:])
                # print(ans,lst, "in")
                return ans
            
            if idx >= len(candidates) or summ > target:
                return
            
            
            lst.append(candidates[idx])
            summ += candidates[idx]
            fun(lst, summ, idx)
            
            summ -= candidates[idx]
            lst.pop()
            
            fun(lst, summ, idx + 1)
        
        
        fun([],0,0)
        return ans
            
        
        