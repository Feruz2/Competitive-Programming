#n,m,a,=list(map(int,input().split()))
n=6
m=6
a=4
width=n-a
height=m-a
if(n%a>0 or m%a>0):
    count=1
else:
    count=0
while(width>0):
    count+=1
    width=width-a
while(height>0):
    count+=1
    height=height-a
print(count)