# 에디터
import sys

input = sys.stdin.readline

n = list(input())

k = int(input())


cursor = len(n)
for i in range(k):
    a = input()
    if a[0] == "P":
        n.insert(cursor, a[2])
        cursor += 1
    elif a[0] == "L":
        if cursor == 0:
            continue
        else:
            cursor -= 1
    elif a[0] == "D":
        if cursor == len(n):
            continue
        else:
            cursor += 1
    elif a[0] == "B":
        if cursor == 0:
            continue
        else:
            del n[cursor - 1]
            cursor -= 1

    if cursor < 0:
        cursor = 0
print("".join(n))
