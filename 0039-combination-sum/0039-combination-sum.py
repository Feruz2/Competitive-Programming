class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def fun(lst, summ, idx):
            
            if summ == target:
                ans.append(lst[:])
                return
            
            if idx >= len(candidates) or summ > target:
                return
            
            lst.append(candidates[idx])
            fun(lst, summ + candidates[idx], idx)
            
            lst.pop()
            fun(lst, summ, idx + 1)
        
        
        fun([],0,0)
        return ans
            
        
        