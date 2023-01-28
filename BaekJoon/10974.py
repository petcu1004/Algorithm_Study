#모든 순열

from itertools import permutations

a=int(input())

arr=[]
for s in range(1, a+1):
    arr.append(s)

for i in permutations(arr):
    print(*i)

# for문 앞의 s가 반복문의 변수 선언을 의미함
# for i in permutations([s for s in range(1, a+1)]): 
#     print(*i)