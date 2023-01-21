# def gen_permutations(arr, n):
#     result=[]

#     if n==0:
#         return [[]]

#     for i, val in enumerate(arr):
#         for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
#             result +=[[val]+P]

#     return result


# arr =[1, 2, 3]
# print(gen_permutations(arr, 2))


def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

permutation([1, 2, 3], 2)