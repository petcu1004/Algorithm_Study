#가장 큰 수

def solution(numbers):
    
    numbers_str=[str(num) for num in numbers]
    numbers_str.sort(reverse=1, key=lambda num:num*3)
    return str(int(''.join(numbers_str)))