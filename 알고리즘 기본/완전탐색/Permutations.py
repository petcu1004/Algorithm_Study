################## 방법 0 - 라이브러리 사용 ##################
# from itertools import permutations

# arr=[1,2,3]
# print(list(permutations(arr,3)))

# ################## 방법 1 - 알고리즘 ##################
# def permutation(arr, r):
#     # 1.
#     arr = sorted(arr) # 정렬
#     used = [0 for _ in range(len(arr))]
#     # print(used)

#     def generate(chosen, used):
#         # 2.
#         if len(chosen) == r:
#             print(chosen)
#             return
	
# 	# 3.
#         for i in range(len(arr)):
#             # print(i)
#             if not used[i]:
#                 # print(i)
#                 # print(used)
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 chosen.pop()
#     generate([], used)

# arr = [1, 2]
# print(permutation(arr, 2))

################## 방법 2 - 알고리즘 ##################
def gen_permutations(arr, n):
    result=[]

    if n==0:
        return [[]]

    for i, val in enumerate(arr):
        # print(arr[:i])
        # print(arr[i+1:])
        # print(n-1)
        for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
            # print(P)
            result +=[[val]+P]

    return result


arr =[1, 2]
print(gen_permutations(arr, 2))

