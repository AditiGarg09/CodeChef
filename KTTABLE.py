# cook your dish here
testcase=int(input())

for i in range(testcase):
    num=int(input())
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    count=0
    for j in range(num):
        if j==0 and a[j]>=b[j]:
            count+=1
        else:
            temp=a[j]-a[j-1]
            if temp>=b[j]:
                count+=1
    print(count)
