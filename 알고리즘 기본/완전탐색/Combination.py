################## 방법 0 - 라이브러리 사용 ##################
# from itertools import combinations

# arr = [1, 2, 3]
# print(list(combinations(arr, 2)))


# ################## 방법 1 - 알고리즘 ##################
# def combination(arr, r):
#     # 1.
#     arr = sorted(arr)

#     # 2.
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#     	# 3.
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         print(arr.index(chosen[-1]))
#         print(start)
#         print(len(arr))
#         for nxt in range(start, len(arr)):
#             print(arr[nxt])
#             chosen.append(arr[nxt])
#             generate(chosen)
#             chosen.pop()
#     generate([])

# combination([1, 2, 3], 2)

################## 방법 2 - 알고리즘 ##################
def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        # print("rest_arr=")
        # print(rest_arr)
        for C in gen_combinations(rest_arr, n-1):
            # print(elem)
            # print(C)
            result.append([elem]+C)
            # print("result=")
            # print(result)
              
    return result

print(gen_combinations([1, 2, 3], 2))
################## 방법 2 - 경우의 수 구하기 ##################
# def choose(n,k):
#     if k == 0: 
#        return 1
#     elif n < k:
#        return 0
#     else:
#         return choose(n-1, k-1) + choose(n-1, k)

# print(choose(3,2))
