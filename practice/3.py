from typing import List
def maxFrequency(nums: List[int], k: int) -> int:
    max_=max(nums)
    final=[0]*(max(nums)+1)

    
    j=0
    count=0
    for i in range(len(nums)-1,0,-1):
        while(nums[i-1]!=nums[i]):
            nums[i-1]+=1
            k-=1
            if(0=k):
                break
 
    for j in range(len(nums)):
        final[nums[j]]+=1
    freq=max(final)
    if(count>=k):
        return freq

nums = [1,4,8,13] 
k = 5
print(maxFrequency(nums,k))