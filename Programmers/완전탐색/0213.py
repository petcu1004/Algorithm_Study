# 소수 찾기

from itertools import permutations

def solution(numbers):
    answer = []
    num=[i for i in numbers]
  
    p=[]    
    for i in range(1,len(numbers)+1):
        p+=list(permutations(num, i))
    
    res=[int(('').join(j)) for j in p]
    
    res=set(res)
    res=list(res)
    print(res)
    
    for i in res:
        if i<2:
            continue
        check=True
        for j in range(2, i):
            if i%j==0: #소수 아님
                check=False
                break
        if check:
            answer.append(i)
    return len(answer)