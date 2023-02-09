#전화번호 목록

def solution(phone_book):
    answer = True
    
    h=dict()
    for i in phone_book:
        h[i] =1 #key는 phone_book이고 value는 1로
        
    for i in phone_book: #i는 119, ...
        s=""
        for j in i: #119일 경우 j는 '1', '1', '9' 순으로
            s+=j #+라는게 문자가 이어지는 것
            if s in h and s!=i: #s in h는 접두사 확인하는 것 / s!=i는 똑같은 119 119의 경우는 제외하기 위해
                answer=False
    return answer