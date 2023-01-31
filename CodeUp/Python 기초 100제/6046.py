# #6046
# n=int(input())
# print(n<<1)

# #6047
# a, b=input().split()
# print(int(a)<<int(b))

# #6048
# a, b=input().split()
# if int(a)<int(b):
#     print(True)
# else:
#     print(False)

# #6049
# a, b=input().split()
# if int(a)==int(b):
#     print(True)
# else:
#     print(False)

# #6050
# a, b=input().split()
# if int(a)<=int(b):
#     print(True)
# else:
#     print(False)

# #6051
# a, b=input().split()
# if int(a)!=int(b):
#     print(True)
# else:
#     print(False)

# #6052 
# n=int(input())
# print(bool(n))

# #6053 
# n=bool(int(input()))
# print(not n)

# #6054 (AND 연산자)
# a, b=input().split()
# print(bool(int(a))and bool(int(b)))

# #6055 (OR 연산자)
# a, b=input().split()
# print(bool(int(a)) or bool(int(b)))

# #6056 (XOR 연산자)
# a, b = input().split()
# c=bool(int(a))
# d=bool(int(b))
# print((c and (not d)) or ((not c) and d))

# #6057
# #잘못된 풀이
# a, b = input().split()
# if(int(a)==int(b)):
#     print("True")
# else:
#     print("False")

# #올바른 풀이
# a, b=input().split()
# a=bool(int(a))
# b=bool(int(b))
# print((a and b) or (not a and not b))
# print(a==b)

# #6058
# a, b=input().split()
# a=bool(int(a))
# b=bool(int(b))
# print(not(a or b))
# print(not a and not b)


