n = int(input())
l = list(map(int, input().split()))  # 수열배열

stack = list()
res = list()  # 정답배열

stack.append(0)
for i in range(1, n):
    while len(stack) != 0 and l[stack[-1]] < l[i]:  # 오큰수를 찾은 것
        res[stack.pop()] = l[i]

    stack.append(i)
while len(stack):  # 오큰수가 없어서 스택에 끝나고 남는 것들 처리
    res[stack.pop()] = -1

print(res)
