#개수 세기

n=int(input())
l=list(map(int, input().split()))
b=int(input())

# res=0
# for i in range(len(l)):
#     if l[i]==b:
#         res+=1

# print(res)

print(l.count(b))