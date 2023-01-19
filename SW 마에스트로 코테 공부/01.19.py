#예산 - Level 1


def solution(d, budget):
    answer = 0
    sum=0
    d.sort() # 정렬되는 함수도 기억해두기!
    for idx, val in enumerate(d): #enumerate 내장 함수 잘 알아두기 -> 인덱스 및 값을 동시에 가져올 수 있음.
        sum+=val
        if budget>=sum:
            answer=idx+1    
        else:
            answer=idx
            break # 맨 처음에 바로 answer을 return하다가 틀린 것을 알고 바로 return을 뒤로 뺐는데 break를 잊어서 for문이 다 돌아가버려 틀리게 됨.
        # 꼼꼼히 확인하기!
    return answer