import sys
sys.setrecursionlimit(109)

def solution(enroll, referral, seller, amount):
    answer = []
    
    d=dict() #연결 고리 트리
    res=dict()
    result=dict()
    
    for i in range(len(enroll)):
        d[enroll[i]]=referral[i]
        res[enroll[i]]=0
        result[enroll[i]]=0
        
    def cal(p):
        if d[p]!='-': #연결되어있는 사람이 있다는 뜻
            person=d[p]
            m=int(res[p]*0.1) ##수수료
            res[p]-=m
            res[person]=m
            cal(person)
        else:
            m=int(res[p]*0.1) ##수수료
            res[p]-=m
            
            for i in range(len(enroll)):
                result[enroll[i]]+=res[enroll[i]]
                res[enroll[i]]=0
    
    for i in range(len(seller)):
        if amount[i]==0:
            continue
        res[seller[i]]=amount[i]*100
        cal(seller[i])
    for i in result:
        answer.append(result[i])
    
    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10] )