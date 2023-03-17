## 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []
    
    n=[]
    m=[]
    for i in range(1, (rows*columns)+1):
        n.append(i)
        if i%columns==0:
            m.append(n)
            n=[]
            
    ro, co= 0, 0      
    print(m)  
    for i in range(len(queries)):
        a=queries[i][0]
        b=queries[i][1]
        c=queries[i][2]
        d=queries[i][3]

        ro=c-a
        co=d-b
        
        tmp=m[a-1][b-1]
        mini=min(tmp, rows*columns)

        print(a, b)
        for j in range(ro):
            m[a-1][b-1]=m[a][b-1]
            mini=min(mini, m[a][b-1])
            a+=1
        
        print(a, b)
        for j in range(co):
            m[a-1][b-1]=m[a-1][b]
            mini=min(mini, m[a-1][b])
            b+=1

        print(a, b) 
        for j in range(ro):
            m[a-1][b-1]=m[a-2][b-1]
            mini=min(mini, m[a-2][b-1])
            a-=1

        print(a, b) 
        for j in range(co-1):
            m[a-1][b-1] = m[a-1][b-2]
            mini=min(mini, m[a-1][b-2])
            b-=1

        m[a-1][b-1]=tmp
        print(m)

        answer.append(mini)

    return answer


print(solution(6, 6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]] ))