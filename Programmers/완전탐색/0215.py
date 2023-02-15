#카펫

def solution(brown, yellow):
    
    for a in range(1, 2502):
        b=int(brown/2)+2-a

        if (a*b) ==(brown+yellow):
            answer=[b, a]
            break

    return answer
