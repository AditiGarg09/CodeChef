# cook your dish here
testcase=int(input())

for i in range(testcase):
    
    lst=input().split(" ")
    x=int(lst[0])
    y=int(lst[1])
    
    num=input()
    
    numOfOne=num.count('1')

    maxLen=0
    count=0
    finalSal=0
    
    for i in range(30):
        if num[i]=='1':
            count+=1
    
        elif num[i]=='0':
            count=0
        
        if count>maxLen:
            maxLen=count
    finalSal=numOfOne*x+maxLen*y
    
    print(finalSal)
