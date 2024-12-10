class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start = hashmap[nums[i]]
            num = len(res)
            for j in range(start, len(res)):
                res.append(res[j] + [nums[i]])
            hashmap[nums[i]] += (len(res) - num) 
        return res
                