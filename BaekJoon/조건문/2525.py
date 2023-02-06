a, b=input().split()
a=int(a)
b=int(b)
c=int(input())

hour=a
min=0

y=b+c

if(y==60):
    hour+=1
    minute=0

elif(y>60):
    hour+=(y//60)
    min=y%60
elif(y<60):
    min=b+c

if(hour>=24):
    hour=hour%24
    
print(hour, min)