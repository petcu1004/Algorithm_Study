#명예의 전당(1)

def solution(k, score):
    answer = []
    
    l=[]
    for i in range(len(score)):
        if(len(l)<k): #명예의 전당
            l.append(score[i])
        else:
            l.append(score[i])
            l.sort(reverse=1)
            l.pop(-1)
            
        l.sort(reverse=1)

        answer.append(min(l))

    return answer