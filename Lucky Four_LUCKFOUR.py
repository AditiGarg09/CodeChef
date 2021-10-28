# cook your dish here
testcase=int(input())
for i in range(testcase):
    num=int(input())
    count=0
    while num>0:
        rem=num%10
        num=num//10
        if rem==4:
            count=count+1
    print(count)
