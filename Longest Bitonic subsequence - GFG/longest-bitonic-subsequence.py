#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		# Code here
        inc = [1] * len(nums)
        dec = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i],inc[j] + 1)
        for i in range(len(nums) - 2 , -1 ,-1):
            for j in range(i,len(nums)):
                if nums[i] > nums[j]:
                    dec[i] = max(dec[i],dec[j] + 1)
        # print(inc,dec)
        
        ans = 0 
        for i in range(len(inc)):
            ans = max(ans,inc[i] + dec[i] - 1)
        return ans 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends