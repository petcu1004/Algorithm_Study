a, b, c = input().split()

a=int(a)
b=int(b)
c=int(c)

res=0

if(a==b and b==c):
    res=10000+a*1000
elif(a==b and b!=c):
    res=1000+a*100
elif(a==c and b!=a):
    res=1000+a*100
elif((b==c and a!=b)):
    res=1000+b*100
elif(a!=b and b!=c and c!=a):
    res=max(a, b)
    res=max(res, c)
    res=res*100

print(res)