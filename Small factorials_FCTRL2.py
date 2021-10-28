# cook your dish here
def fact(num):
    if num<=1:
        return 1
    else:
        return(num*fact(num-1))

testcase=int(input())
for i in range(testcase):
    num=int(input())
    print(fact(num))
