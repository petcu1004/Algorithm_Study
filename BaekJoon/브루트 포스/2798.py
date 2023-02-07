# from itertools import combinations

# a, b=map(int, input().split())
# l=list(map(int, input().split()))
# res=list(combinations(l, 3))

# z=[]
# for i in range(len(res)):
#     z.append(sum(res[i]))
# z.sort(reverse=1)

# for i in range(len(res)-1):
#     if z[i]<=b:
#         print(z[i])
#         break
        

#-------------------------------------------#

n, m=map(int, input().split())
arr=sorted(list(map(int, input().split())), reverse=True)

mx=0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(i+2, n):
            s=arr[i]+arr[j]+arr[k]
            if s<=m:
                if mx<s:
                    mx=s
                    break

print(mx)