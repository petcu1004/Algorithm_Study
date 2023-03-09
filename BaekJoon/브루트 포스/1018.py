## 체스판 다시 칠하기 - 실버 4

a, b= map(int, input().split())

n=[]
for i in range(a):
    k=list(input())
    n.append(k)

x=0

# for _ in range(a):
#     n+=list(input())
    
# for i in range(a*b):

#     if a%(i+1)==0:
        
#         k=n[0]



for i in range(a):
    k=n[i][0]
    for j in range(b):
        if j%a==0:
            if k=='W':
                k='B'
            else:
                k='W'


        
        if n[i][j]!=k:
            k=n[i][j-1]
            print(i, j)
            x+=1
        else:
            k=n[i][j-1]

print(x)