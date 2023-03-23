## 플로이드
import sys
from math import inf
input=sys.stdin.readline

n=int(input())
m=int(input())
res=[[inf]*n for _ in range(n)]


def floydWarshall():
    for i in range(m):
        a, b, c = map(int, input().split())
        if res[a-1][b-1]>c:
            res[a-1][b-1] = c
        #res[a-1][b-1] = min(res[a-1][b-1], c)

    for k in range(n): #k = 거쳐가는 노드
        res[k][k]=0 #자기 자신의 노드는 0으로 처리
        for i in range(n): #i = 출발 노드
            for j in range(n): #j = 도착 노드
                # res[i][j]=min(res[i][j], res[i][k]+res[k][j])
                if res[i][k]+res[k][j] < res[i][j]:
                    res[i][j] = res[i][k] + res[k][j]

    for i in range(n):
        for j in range(n):
            if res[i][j]==inf:
                res[i][j]=0
            print(res[i][j], end=' ')
        print()

floydWarshall()