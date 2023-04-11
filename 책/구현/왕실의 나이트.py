n=input()
row=int(n[1])
column=ord(n[0])- ord('a')+1

steps=[(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

cnt=0
for i in steps:
    nx=row+i[0]
    ny=column+i[1]

    if nx<1 or nx>8 or ny<1 or ny>8:
        continue
    else:
        cnt+=1


print(cnt)