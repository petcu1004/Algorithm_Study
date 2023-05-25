n, k = map(int, input().split())

table = list()
for i in range(n):
    table.append(i + 1)

res = list()
start = 0
# print("<")
while len(table) != 0:
    if start == len(table):
        start = 0
    print(table[start + 2] + ", ")
    table[start]
    table.pop(table[start + 2])

    start += 2
