def fact(num):
    if num <= 1:
        return 1
    else:
        return(num*fact(num-1))

t=int(input())
for i in range(t):
    num = int(input())
    print(fact(num))
