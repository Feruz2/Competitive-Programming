nums = [1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]

k = 2
count=0
removed=0
for i in range(len(nums)-removed):
    for j in range(len(nums)-removed):
        if(nums[i]+nums[j]==k and i!=j):
            nums.remove(nums[i])
            nums.remove(nums[j])
            count+=1
            removed+=2
print(count)
