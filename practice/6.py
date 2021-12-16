nums =  [3,1,3,4,3]
k = 6
count=0
for i in range(len(nums)-2*(count)):
    for j in range(len(nums)-2*(count)):
        if(nums[i]+nums[j]==k and i!=j ):
           nums.remove(nums[i])
           nums.remove(nums[j])
           count+=1
print( count)