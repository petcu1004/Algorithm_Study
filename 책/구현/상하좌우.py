a=int(input())
maps=[[0]*(a+1) for _ in range(a+1)]

x, y =1, 1
b=list(map(str, input().split()))

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]


for i in b:
    if i=='R':
        nx=x+dx[0]
        ny=y+dy[0]
    elif i=='L':
        nx=x+dx[1]
        ny=y+dy[1]

    elif i=='U':
        nx=x+dx[3]
        ny=y+dy[3]

    elif i=='D':
        nx=x+dx[2]
        ny=y+dy[2]

    if nx<=0 or nx>=len(maps) or ny<=0 or ny>=len(maps[0]):
        continue
    else:
        x=nx
        y=ny
        
print(x, y)


