##로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    a, b =0, 0
    for i in lottos:
        if i in win_nums:
            a+=1
        if i==0: ## b=lottos.count(0)으로 코드 대체 가능
            b+=1

    return rank[a+b], rank[a]