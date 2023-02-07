l=[]

for _ in range(9):
    row=list(map(int, input().split()))
    l.append(row)
    
res=l[0][0]

for i in range(9):
    for j in range(9):
        if res<l[i][j]:
            res=l[i][j]

print(res)

for i in range(9):
    for j in range(9):
        if res==l[i][j]:
            print(i+1, j+1, end=' ')
            break

# newlist=[(i,j) for i in range(9) for j in range(9) if l[i][j]==res]
# print(newlist)