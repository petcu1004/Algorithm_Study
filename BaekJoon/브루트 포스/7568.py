## 덩치 - 실버5

n=int(input())

res=[]
answer=[]

for i in range(n):
    a, b = map(int, input().split())
    res.append([a, b])

for i in range(n):
    k=0
    for j in range(n):        
        if res[i][0] < res[j][0]:
            if res[i][1] < res[j][1]:
                k+=1
            else:
                continue
        else:
            continue
            
    answer.append(k+1)



# for i in answer:
#      print(i, end=' ')    

print(*answer)