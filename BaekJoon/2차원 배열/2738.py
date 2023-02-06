a, b =map(int, input().split())


A, B=[], []

for _ in range(a):
    row=list(map(int, input().split()))
    A.append(row)

for _ in range(a):
    row=list(map(int, input().split()))
    B.append(row)

res=[]
for i in range(len(A)):
    for j in range(len(B)):
        print(A[i][j]+B[i][j], end=' ')
    print()
