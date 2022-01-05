# cook your dish here
t = int(input())
for i in range(t):
    num=list(map(int, input().split()))
    if num[0]>num[1]:
        print(">")
    elif num[0]==num[1]:
        print("=")
    else:
        print("<")
