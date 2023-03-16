##로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = [0, 0]
    a, b, d =0, 0, 0
    for i in lottos:
        if i in win_nums:
            a+=1
        elif i==0:
            b+=1
        else:
            d+=1

    corr=a+b
    wrong = 6-(b+d)
    c, w=0, 0
    if corr==6:
        answer[0]=1
    elif corr==5:
        answer[0]=2
    elif corr==4:
        answer[0]=3
    elif corr==3:
        answer[0]=4
    elif corr==2:
        answer[0]=5
    else:
        answer[0]=6
        
    if wrong==6:
        answer[1]=1
    elif wrong==5:
        answer[1]=2
    elif wrong==4:
        answer[1]=3
    elif wrong==3:
        answer[1]=4
    elif wrong==2:
        answer[1]=5
    else:
        answer[1]=6
    
    return answer