import math

def solution(enroll, referral, seller, amount):
    answer = []
    
    d=dict() #연결 고리 트리
    res=dict()
    result=dict()
    for i in range(len(enroll)):
        d[enroll[i]]=referral[i]
        res[enroll[i]]=0
        result[enroll[i]]=0
        
    print(d)
    

    # for i in range(len(seller)):
        # res[seller[i]]=amount[i]*100
    
    # print(res)
    def cal(p):
        if d[p]!='-': #연결되어있는 사람이 있다는 뜻
            person=d[p]
            print(person)
            # n=int(res[p]*0.9) ##자신의 이득
            m=int(res[p]*0.1) ##수수료
            res[p]-=m
            res[person]+=m
            print(res)
            cal(person)
        else:
            m=math.floor(res[p]*0.1) ##수수료
            print(m)
            res[p]-=m
            
            for i in range(len(enroll)):
                result[enroll[i]]+=res[enroll[i]]
                res[enroll[i]]=0
            print(res)
            print(result)
        
        return
    
    for i in range(len(seller)):
        res[seller[i]]=amount[i]*100
        print("값 넣어줌")
        # if d[seller(i)]!='-': #연결되어있는 사람이 있다는 뜻
        cal(seller[i])
            
            
        #     person=d[seller(i)]
        #     n=am[i]*0.9 ##자신의 이득
        #     m=am[i]*0.1 ##수수료
        #     res[seller(i)]=n
        #     res[person]=m
        
    for i in result:
        answer.append(result[i])
    
    return answer