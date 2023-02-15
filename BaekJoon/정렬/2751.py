# 수 정렬하기 2
import sys

n=int(input())
l=[]

for _ in range(n):
    l.append(int(sys.stdin.readline()))

# l.sort()
for i in sorted(l):
    print(i)
    # sys.stdout.write(str(i)+'\n')


# def sol():
#     a=[None]*2000001
#     b=map(int,open(0))
#     next(b)
#     for i in b:a[i]=1
#     print("\n".join(str(i) for i in range(-1000000,1000001,1) if a[i]))

# sol()