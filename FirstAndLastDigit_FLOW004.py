# cook your dish here
testcase=int(input())

for i in range(testcase):
    num=int(input())
    lastNum=num%10
    
    while num>0:
        firstNum=num%10
        num=num//10
    
    print(firstNum+lastNum)
