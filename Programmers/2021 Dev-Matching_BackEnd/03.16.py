##로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    k=0
    n=0
    for i in lottos:
        # print(i)
        if i in win_nums:
            # print("존재")
            k+=1
        else:
            n+=1
        if i==0:
            k+=1
        if i==0:
            n+=1
    
    # if k==6:
    #     answer.append(1)
    # elif k==5:
    #     answer.append(2)
    # answer=[7-k, 7-]   
    answer.append(7-k)
    if n>5:
        answer.append(6)
    else:
        answer.append(7-n)
    
    return answer