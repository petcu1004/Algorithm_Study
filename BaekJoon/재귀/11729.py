# 하노이 탑 이동 순서

# def hanoi(n, start, end) :
#     if n==1:
#         print(start, end)
#         return
    
#     hanoi(n-1, start, 6-start-end)
#     print(start, end)
#     hanoi(n-1, 6-start-end, end)

# n = int(input())
# print(2**n -1)
# hanoi(n, 1, 3)


def hanoi(n, a, b, c):
    if n==1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move. append([a, c])
        hanoi(n-1, b, a, c)

move=[]
hanoi(int(input()), 1, 2, 3)
print(len(move))
print("\n".join([' '.join(str(i) for i in row) for row in move]))

