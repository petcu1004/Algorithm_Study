## 체스판 다시 칠하기 - 실버 4

a, b= map(int, input().split())

n=[]
m=[]
for _ in range(a):
    k=input()
    m.append(k)

x=0
res=[]

cl=[]
dl=[]

c='W'
d='B'

cl.append(c)
dl.append(d)

for j in range(63):
    if cl[j]==c and (j+1)%8!=0:
        cl.append(d)
        dl.append(c)
    elif cl[j]==d and (j+1)%8!=0:
        cl.append(c)
        dl.append(d)
    elif cl[j]==c and (j+1)%8==0:
        cl.append(c)
        dl.append(d)
    elif cl[j]==d and (j+1)%8==0:
        cl.append(d)
        dl.append(c)

x, y=0, 0

for i in range(a-7):
    for j in range(b-7):
        for e in range(i, i+8):
            for f in range(j, j+8):
                n.append(m[e][f])
   
        for r in range(64):
            if n[r]!=cl[r]:
                x+=1
            if n[r]!=dl[r]:
                y+=1
            
        
        res.append(x)
        res.append(y)
        n=[]
        x=0
        y=0

print(min(res))