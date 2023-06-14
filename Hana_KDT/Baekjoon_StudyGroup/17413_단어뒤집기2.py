import sys

word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":  # 열린 괄호를 만나면
        i += 1
        while word[i] != ">":  # 닫힌 괄호를 만날 때 까지
            i += 1
        i += 1  # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum():  # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        tmp = word[start:i]  # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()  # 뒤집는다
        word[start:i] = tmp
    else:  # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i += 1  # 그냥 증가시킨다

print("".join(word))


# a = list(input().split(""))

# rev = []
# origin = []
# result = []
# k = 0
# for i in range(len(a)):
#     word = list(a[i])
#     # print(word)
#     for j in range(len(word)):
#         if word[j] == "<":
#             if len(rev) != 0:
#                 for x in range(len(rev) - 1, -1, -1):
#                     origin.append(rev[x])
#                 rev = []
#             k = 1
#             origin.append("<")
#         elif word[j] == ">":
#             k = 0
#             origin.append(">")
#         elif k == 0:
#             rev.append(word[j])

#         elif k == 1:
#             origin.append(word[j])

#     if len(rev) != 0:
#         for x in range(len(rev) - 1, -1, -1):
#             origin.append(rev[x])
#         origin.append(" ")
#         rev = []
#     print("".join(origin))
