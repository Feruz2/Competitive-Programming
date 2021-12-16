nums=[0,1,3,5,4]
nums.sort()
if(len(nums)==3):
    if(((nums[0] + nums[2]) /2 )==nums[1]):
        nums[0],nums[1]=nums[1],nums[0]
       # print(  nums)
for i in range(1,len(nums)-1):
    if(i==len(nums)-2):
        if(((nums[i-1] + nums[i+1]) /2 )==nums[i]):
            nums[i],nums[i+1]=nums[i+1],nums[i]
            print(nums)
    elif(((nums[i-1] + nums[i+1]) /2 )==nums[i]):
        nums[i+1],nums[i+2]=nums[i+2],nums[i+1]
   
        print(nums)
    
            
        
        
#print(nums)

        