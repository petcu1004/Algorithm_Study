#멀쩡한 사각형 - Level 2

import math

def solution(w,h):
    answer= w*h - (w+h-math.gcd(w, h))
    
    return answer