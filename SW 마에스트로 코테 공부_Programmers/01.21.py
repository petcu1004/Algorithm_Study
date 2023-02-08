#소수 만들기 - Level 1

from itertools import combinations

def solution(nums):
    answer = 0
    combi=list(combinations(nums, 3))

    for i in range(len(combi)): #만들어질 수 있는 경우의 수
        sum=0
        for j in range(3): # 어차피 3개의 숫자를 뽑음 / combo[j]는 튜플 값
            
            # print((combi[i])[j])
            val=(combi[i])[j]
            sum=sum+val
            
        #소수인지 확인
        x=0
        for k in range(2,sum):
            if ( sum % k ==0):
                x=x+1

        if(x==0) :
            answer=answer+1
                    
    return answer