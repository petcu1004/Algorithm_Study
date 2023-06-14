n = int(input())

stack = list()
count = 0
# stack.append(0)
for i in range(n):
    a = int(input())
    if len(stack) == 0:
        for i in range(a):
            count += 1
            stack.append(count)
            print("+")
    else:
        while 1:
            if a < stack[-1]:
                print("-")
                stack.pop()

            elif a > stack[-1]:
                count += 1
                stack.append(count)
                print("+")
            else:
                print("-")
                stack.pop()

    print(stack)
