n = int(input())

l = list()
for i in range(n):
    l.append(int(input()))


print(l)

count = 1
stack = list()

flag = 1
for i in range(len(l)):
    while len(stack) != l[i]:
        stack.append(count)
        count += 1
        print("+")
        flag = 0
        if stack[-1] == l[i]:
            print("-")
            stack.pop()

        elif stack[-1] < l[i] and flag == 0:
            stack.append(count)
            count += 1
            print("+")

        elif stack[-1] < l[i] and flag == 1:
            print("No")
            break

    flag = 0
