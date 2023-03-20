# 폰켓몬

def solution(nums):
    answer = 0
    
    n=set(nums)
    n=len(n)
    if n>=(len(nums)//2):
        answer=len(nums)//2
    else:
        answer=n  
    
    return answer