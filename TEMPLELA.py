# cook your dish here
testcase=int(input())
for i in range(testcase):
    n=int(input())
    h=list(map(int,input().split(" ")))
    
    if n%2==0:
        print("no")
    elif h[0]!=1:
        print("no")
    else:
        h1=h.copy()
        h1.reverse()
        
        if h==h1:
            temp=n//2
            for i in range(temp):
                if h[i]==(i+1):
                    flag=1
                else:
                    flag=0
                    break
            
            if flag==0:
                print("no")
            else:
                for i in range(temp+1,n,1):
                    if h[i]==(h[i-1]-1):
                        flag=1
                    else:
                        flag=0
                        break
                if flag==0:
                    print("no")
                else:
                    print("yes")
        else:
            print("no")
