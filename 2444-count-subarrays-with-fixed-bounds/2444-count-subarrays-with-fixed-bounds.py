class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l = len(nums)
        res = 0
        left = 0
        count_min, count_max = 0, 0
        start = 0
        for right in range(l):
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
                count_min = 0
                count_max = 0
                start = left
                continue
            
            if nums[right] == minK:
                count_min += 1
            
            if nums[right] == maxK:
                count_max += 1

            while start <= right and count_min and count_max:
                if nums[start] == minK:
                    count_min -= 1

                if nums[start] == maxK:
                    count_max -= 1

                start += 1

            res += max(0, start - left)
        return res