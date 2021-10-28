# cook your dish here
testcase=int(input())

for i in range(testcase):
    
    n,k=map(int,input().split(" "))
    scores=list(map(int,input().split(" ")))
    scores.sort(reverse=True)
    
    count=0
    for j in range(n):
        if scores[j]>=scores[k-1]:
            count+=1
    
    print(count)
