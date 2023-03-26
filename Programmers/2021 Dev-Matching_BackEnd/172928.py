from collections import deque
def solution(park, routes):
    answer = []
    a, b=0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                a=i
                b=j
     
    moveX=dict()
    moveY=dict()
    moveX={'E':0, 'W':0, 'S': 1, 'N' : -1}
    moveY={'E':1, 'W':-1, 'S': 0, 'N' : 0}
    
    for i in range(len(routes)):
        kx, ky=0, 0
        for j in range(int(routes[i][2])):
            
            nx=a+moveX[routes[i][0]]
            ny=b+moveY[routes[i][0]]

            if 0>nx or nx>=len(park) or 0>ny or ny>=len(park[0]):
                a-=kx
                b-=ky
                break
            if park[nx][ny]=='X':
                a-=kx
                b-=ky
                break
            else:
                a=nx
                kx+=moveX[routes[i][0]]
                b=ny
                ky+=moveY[routes[i][0]]

    return [a, b]