#H-Index

#오름차순
def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    return 0


#내림차순
def solution(citations):
    citations.sort(reverse=1)
    
    for i in range(len(citations)):
        if citations[i]<=i:
            return i
    return len(citations) #citations 배열 모두 인용된 것으로 간주됨