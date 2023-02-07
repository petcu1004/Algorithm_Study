a=int(input())
l=[]
for i in range(a):
    x=int(input())
    l.append(x)

l.sort()

for i in range(len(l)):
    print(l[i])

#----------------------------------------------------#

#다른 사람 코드
import sys

n=int(input())
l=[int(sys.stdin.readline()) for _ in range(n)]

for i in sorted(l):
    print(i)

#----------------------------------------------------#

#다른 사람 코드
import sys

input=sys.stdin.readline
n=int(input())

for i in sorted([int(input()) for _ in range(n)]):
    print(i)