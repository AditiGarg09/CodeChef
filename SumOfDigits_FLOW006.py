# cook your dish here
testcase=int(input())

for i in range(testcase):
    num=int(input())
    sum1=0
    rem=0
    while num>0:
        rem=num%10
        sum1=sum1+rem
        num=num//10
    print(int(sum1))
