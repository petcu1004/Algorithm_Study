##공원 산책

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
        print(routes[i][0], routes[i][2])
        kx, ky=0, 0
        for j in range(int(routes[i][2])):
            
            nx=a+moveX[routes[i][0]]
            ny=b+moveY[routes[i][0]]
            print(nx, ny)
            
            if 0>nx or nx>=len(park) or 0>ny or ny>=len(park[0]):
                # continue
                print("벽")
                # a=nx-kx
                # b=ny-ky
                break
            if park[nx][ny]=='X':
                # continue
                print("장애물")
                # a=nx-kx
                # b=ny-ky
                break
            else:
                a=nx
                kx=a+nx
                b=ny
                ky=b+ny
            

    return answer