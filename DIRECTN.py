# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    direction=input()
    flag=0
    for j in range(n):
        if j!=(n-1):
            if direction[j]==direction[j+1]:
                flag=1
                # print(direction[j]," ",direction[j+1])
                break
        
    if flag==1:
        print("Yes")
    else:
        print("No")
