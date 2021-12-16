arr=[]
path="DDUUDDUDUUUD"
step=12
for letter in path:
    if(letter=="U"):
        arr.append(1)
    else:
        arr.append(-1)
print(arr)
total=0
count=0
for i in range(step):
    total=total+arr[i]
    if(total==0 and arr[i]==(1)):
        count+=1
print(count)        