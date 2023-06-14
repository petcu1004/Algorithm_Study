n = int(input())
m = int(input())

a = list(map(int, input().split()))

a.sort()

# print(a)

i = 0
j = len(a) - 1
sum = 0
count = 0
while i < j:
    sum = a[i] + a[j]
    if sum < m:
        i += 1
    elif sum > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
    sum = 0

print(count)
