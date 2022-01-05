# cook your dish here
t=int(input())
a=[]
b=[]
c=[]
for i in range(t):
    num=list(map(int,input().split()))
    a.append(num[0])
    b.append(num[1])

for j in range(len(a)):
    if j!=0:
        a[j]+=a[j-1]
        b[j]+=b[j-1]

for k in range(len(a)):
    if a[k]>b[k]:
        c.append(a[k]-b[k])
    else:
        c.append(b[k]-a[k])
maxC=max(c)
index=c.index(maxC)
if a[index]>b[index]:
    print("1 ",maxC)
else:
    print("2",maxC)
