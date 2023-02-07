#메모리, 시간 제일 작음 라지만 코드 길이가 가장 김.
a=0
list=[]
for _ in range(5):
    x = int(input())
    a+=x
    list.append(x)

print(a//5)
list.sort()
print(list[2])
#-----------------------------------------------#

import sys
x=sorted([int(sys.stdin.readline()) for _ in range(5)])
print(sum(x)//5)
print(x[2])

#-----------------------------------------------#
#메모리, 시간 다 긴데 코드 길이가 가장 짧음..
l=sorted([int(input()) for _ in range(5)])
print(sum(l)//5) #sum()함수를 쓰면 되는구나..!
print(l[2])