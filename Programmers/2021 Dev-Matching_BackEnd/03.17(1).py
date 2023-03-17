def solution(enroll, referral, seller, amount):
    
    money = dict((e, 0) for e in enroll)
    head = dict((e, r) for e, r in zip(enroll, referral))
    
    for name, m in zip(seller, amount):
        price = 100*m
        
        while True:
            if name =="-" or price <=0:
                break
            next_money = int(price *0.1)
            money[name] += price - next_money
            # print(money)
            
            name = head[name]
            price = next_money
            
    return list(money.values())

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10] )