class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        def fun(lst, summ, idx):
           
            if summ == target:
                ans.append(lst[:])
                return
            if summ > target:
                return 
            for i in range(idx, len(candidates)):
                
                if i != idx and candidates[i] == candidates[i - 1]: continue
                
                lst.append(candidates[i])
                fun(lst, summ + candidates[i], i + 1)
                lst.pop()
                


        fun([],0,0)
        return ans