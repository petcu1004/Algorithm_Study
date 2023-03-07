## 분해합

# n=input()
# l=len(n)

# i=1
# n=int(n)

# while n!=i:
#     res=[]

#     i=str(i)
#     x=len(i)
#     for k in range(x):
#         res.append(int(i[k]))


#     i=int(i)
#     res.append(i)

#     if sum(res) == n:
#         print(i)
#         break    
#     i+=1
# if(n==i):
#     print(0)


N=input()
k=len(N)
N=int(N)
if N>=9*k:
    for i in range(N-9*k,N+1):
        n = i
        p = str(i)
        for j in range(0, len(p)):
            n += int(p[j])
        if n==N:
            print(i)
            quit()
else:
    for i in range(0,N+1):
        n = i
        p = str(i)
        for j in range(0, len(p)):
            n += int(p[j])
        if n==N:
            print(i)
            quit()
print(0)




n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)