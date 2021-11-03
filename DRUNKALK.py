# cook your dish here
testcase=int(input())
for i in range(testcase):
    k=int(input())
    count=0
    for j in range(1,(k+1),1):
        if j%2==0:
            count-=1
        else:
            count+=3
    print(count)
