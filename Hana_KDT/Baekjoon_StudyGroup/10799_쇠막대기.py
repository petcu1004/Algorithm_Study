a = list(input())

s = list()
res = 0
for i in range(len(a)):
    if a[i] == "(":
        s.append(a[i])
    else:  #')'을 만나면
        if a[i - 1] == "(":
            s.pop()
            res += len(s)
        else:
            s.pop()
            print(i)
            res += 1
print(res)
