#멀쩡한 사각형 - Level 2

import math

def solution(w,h):
    #최대 공약수를 구하는 함수 gcd()
    answer= w*h - (w+h-math.gcd(w, h))
    
    return answer