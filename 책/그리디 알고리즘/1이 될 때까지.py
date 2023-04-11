a, b = map(int, input().split())

cnt=0
while(1):
    if a==1:
        print(cnt)
        break

    if a%b==0:
        cnt+=1
        a=a//b
    else:
        cnt+=1
        a-=1
    
