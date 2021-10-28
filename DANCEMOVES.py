# cook your dish here
testcase=int(input())

for i in range(testcase):
    x,y=map(int,input().split(" "))
    stepsCount=0
    
    while x!=y:
        if (x+2)<=y:
            x=x+2
        else:
            x=x-1
        stepsCount=stepsCount+1
    
    print(stepsCount)
