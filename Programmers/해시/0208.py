#폰켓몬

from itertools import combinations

def solution(nums):
    answer = 0

    num_len=len(set(nums)) #중복 없앤 애들 = 종류 개수 최대값
    res=len(nums)//2 #최대로 나올 수 있는 경우의 수
    if res < num_len:
        answer=res
    else:
        answer=num_len
    
    return answer