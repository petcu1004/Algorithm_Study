# 에디터

n=list(input())

k=int(input())


x=len(n)
for i in range(k):
    print(x)
    a=input()
    if a[0]=="P":
        n.insert(x,a[1])
        x=len(n)
    elif a[0]=="L":
        if x==0:
            continue
        else:
            x-=1
    elif a[0]=="D":
        if x==len(n)-1:
            continue
        else:
            x+=1
    elif a[0]=="B":
        if x==0:
            continue
        else:
            x-=1
print(''.join(n))

