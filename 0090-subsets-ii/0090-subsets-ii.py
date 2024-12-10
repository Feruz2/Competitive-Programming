class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        sett = set()
        nums.sort()
        ans = []
        def fun(lst, idx):
            if idx >= len(nums):
                sett.add(tuple(lst))
                return  
            lst.append(nums[idx])
            fun(lst, idx + 1)
            
            lst.pop()
            fun(lst, idx + 1)
        
        
        fun([], 0)
        
        for elt in sett:
            ans.append(list(elt))
        return ans
        