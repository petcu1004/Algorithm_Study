s=list(input())
res=list()

p=len(s)
for i in range(p):
    k=""
    for j in range(len(s)):
        k+="".join(s[j])
    res.append(k)
    s.pop(0)
    
res.sort()
for i in range(p):
    print(res[i])