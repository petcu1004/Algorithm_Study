## 당구 연습


def solution(m, n, startX, startY, balls):
    answer = []
    mini=[]
    
    for i in range(len(balls)):
        if startX == balls[i][0] and startY != balls[i][1]:
            x=(m-balls[i][0])*2
            y=abs(balls[i][1]-startY)
            res=(x**2)+(y**2)
            answer.append(res)
        elif startX != balls[i][0] and startY == balls[i][1]:
            x=abs(balls[i][0]-startX)
            y=(n-balls[i][1])*2
            res=(x**2)+(y**2)
            answer.append(res)
        elif startX != balls[i][0] and startY != balls[i][1]: #치는 방법의 수가 많음
            # 왼쪽 벽면에 부딪힐때
            x=abs(balls[i][0]-startX)
            y=abs(balls[i][1]+startY)
            res=(x**2)+(y**2)
            mini.append(res)
            
#             # 위쪽 벽면에 부딪힐때
#             x=abs(balls[i][0]-startX)
#             y=(abs(n-balls[i][1])*2) - abs(startY-balls[i][1])
#             res=(x**2)+(y**2)
#             mini.append(res)
            
#             # 오른쪽 벽면에 부딪힐때
#             x=abs(balls[i][0]+startX)
#             y=abs(balls[i][1]-startY)
#             res=(x**2)+(y**2)
#             mini.append(res)
            
#             # 아래쪽 벽면에 부딪힐때
#             x=abs(startX-balls[i][0])
#             y=abs(startX+balls[i][0])
#             res=(x**2)+(y**2)
#             mini.append(res)
#             # print(mini)
            
            # 대각선상에 있을 때 왼쪽 위 대각선
            x=abs(balls[i][0]-startX)
            y=abs(balls[i][1]-startY)
            a=(x**2)+(y**2)
            x=abs(m-balls[i][0])
            y=abs(n-balls[i][1])
            b=((x**2)+(y**2)) * 2
            res=a+b
            mini.append(res)
            
            # 대각선상에 있을 때 오른쪽 아래 대각선
            x=abs(startX-m)
            y=abs(startY)
            a=(x**2)+(y**2) *2
            x=abs(balls[i][0]-startX)
            y=abs(balls[i][1]-startY)
            b=(x**2)+(y**2)
            res=a+b
            mini.append(res)
            
            # 대각선상에 있을 때 오른쪽 위 대각선
            x=abs(balls[i][0]-startX)
            y=abs(balls[i][1]-startY)
            a=(x**2)+(y**2)
            x=abs(m-balls[i][0])
            y=abs(n-balls[i][1])
            b=((x**2)+(y**2)) * 2
            mini.append(a+b)
            
            # 대각선상에 있을 때 왼쪽 아래 대각선
            x=abs(startX)
            y=abs(startY)
            a=(x**2)+(y**2) *2
            mini.append(res)
            x=abs(balls[i][0]-startX)
            y=abs(balls[i][1]-startY)
            b=(x**2)+(y**2)
            mini.append(a+b)
            
            
            # print(mini)
            k=min(mini)
            answer.append(k)

    
    return answer