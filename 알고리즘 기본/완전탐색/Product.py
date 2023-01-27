from itertools import product

for i in product([1,2,3], repeat=2):
    print(i, end=" ")


