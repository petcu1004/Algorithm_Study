a, b=input().split()

a=int(a)
b=int(b)

if(b-45<0):
    x=b-45
    if(a==0):
        a=24
    print(a-1, 60+x)

else:
    print(a, b-45)