# cook your dish here
size=int(input())
lst=[]
for i in range(size):
    num=int(input())
    lst.append(num)

lst=sorted(lst)

for i in range(size):
    print(lst[i])
