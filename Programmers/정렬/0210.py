#K번째수

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        a=commands[i][0]
        b=commands[i][1]
        c=commands[i][2]
        res=array[a-1:b]
        res.sort()
        answer.append(res[c-1])    
    return answer