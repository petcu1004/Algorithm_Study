## N으로 표현

def solution(N, number):
    if number == 1:
        return 1
    set_list = []
    
    for cnt in range(1, 9): # 1개부터 8개까지 확인
        # 1. [ SET x 8 ] 초기화 
        partial_set = set() # 2. 각 set마다 기본 수 "N" * i 수 초기화
        
                # 3. n 일반화
    #   { 
    #       "n" * i U 
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set, 
    #    } 
    # number를 가장 최소로 만드는 수 구함.
        partial_set.add(int(str(N) * cnt)) # 이어 붙여서 만드는 경우 넣기
        for i in range(cnt - 1): # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    
                    if op2 != 0:
                        partial_set.add(op1 // op2)
        # 만든 집합에 number가 처음 나오는지 확인
        if number in partial_set:
            return cnt
        set_list.append(partial_set)
    return -1