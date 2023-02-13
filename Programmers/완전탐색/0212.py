#모의고사

def solution(answers):
    answer = []
    a=[1, 2, 3, 4, 5]
    b=[2, 1, 2, 3, 2, 4, 2, 5]
    c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result=[0, 0, 0]
    
    for i in range(len(answers)):
        if(answers[i]==a[i%5]):
            result[0]+=1
        if(answers[i]==b[i%8]):
            result[1]+=1
        if(answers[i]==c[i%10]):
            result[2]+=1

    for i in range(len(result)):
        if result[i]==max(result):
            answer.append(i+1)

    
    return answer