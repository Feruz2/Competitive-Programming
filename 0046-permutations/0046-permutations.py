class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        def rec(idx, lst, sett):
            if len(lst) ==  len(nums):
                ans.append(lst)
                return

            for i in range(len(nums)):
                if i not in sett:
                    sett.add(i)
                    rec(i + 1, lst + [nums[i]], sett)
                    sett.remove(i)

        
        rec(0,[], set())
        return ans