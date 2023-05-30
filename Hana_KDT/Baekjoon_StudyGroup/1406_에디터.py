# 에디터 - 성공
import sys

input = sys.stdin.readline

l_stack = list(input().strip())

r_stack = list()
k = int(input())

for i in range(k):
    a = input()
    if a[0] == "P":
        l_stack.append(a[2])
        # cursor += 1
    elif a[0] == "L":
        if len(l_stack)==0:
            continue
        else:
            r_stack.append(l_stack.pop(-1))
    elif a[0] == "D":
        if len(r_stack)==0:
            continue
        else:
            l_stack.append(r_stack.pop(-1))
    elif a[0] == "B":   
        if len(l_stack)==0:
            continue
        else:
            l_stack.pop(-1)

for i in reversed(range(len(r_stack))):
    l_stack.append(r_stack[i])

print("".join(l_stack))
