n = int(input())

for i in range(n):
    ip = list(map(int, input().split(" ")))

    count = 0
    x = 0
    y = 0
    k = 0  # 카잉 달력으로 표현하지 못하는 유효하지 않은 표현일 경우
    while x != ip[0] or y != ip[1]:
        if (x == ip[2]) and (y == ip[3]):
            # print(count)
            k += 1
            break
        else:
            if x < ip[0]:
                x += 1
            else:
                x = 1
            if y < ip[1]:
                y += 1
            else:
                y = 1
            # print(x, y, count)
            k = -1
            count += 1
    if k == 0:
        print(-1)
    elif k == -1:  # 1 1 1 1일 떄..
        print(1)
