# import sys
# input=sys.stdin.readline
# n = int(input())

# arr = list()
# for i in range(n):
#     a = input().split()
#     if a[0] == "add":
#         if int(a[1]) not in arr:
#             arr.append(int(a[1]))
#         else:
#             continue
#     elif a[0] == "remove":
#         if int(a[1]) in arr:
#             arr.remove(int(a[1]))
#         else:
#             continue
#     elif a[0] == "check":
#         if int(a[1]) in arr:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == "toggle":
#         if int(a[1]) in arr:
#             arr.remove(int(a[1]))
#         else:
#             arr.append(int(a[1]))
#     elif a[0] == "all":
#         arr = list()
#         for i in range(1, 21):
#             arr.append(i)
#     elif a[0] == "empty":
#         arr = list()

######################################################

import sys

m = int(sys.stdin.readline())
bit = 0
for _ in range(m):
    command = sys.stdin.readline().split()

    if command[0] == "all":
        bit = (1 << 20) - 1
    elif command[0] == "empty":
        bit = 0
    else:
        op = command[0]
        num = int(command[1]) - 1

        if op == "add":
            bit |= 1 << num
        elif op == "remove":
            bit &= ~(1 << num)
        elif op == "check":
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        elif op == "toggle":
            bit = bit ^ (1 << num)
