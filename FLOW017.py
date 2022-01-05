# cook your dish here
t=int(input())
for i in range(t):
    lst=list(map(int,input().split(" ")))
    maxlst=max(lst)
    minlst=min(lst)
    for j in range(3):
        if lst[j]>minlst and lst[j]<maxlst:
            print(lst[j])
            break
