#위장

def solution(clothes):
    closet={}
    result=1

    for element in clothes:
        key=element[1]
        value=element[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key]=[value]
            
        print(closet)
        
    
    for key in closet.keys():
        result=result * (len(closet[key]) +1)
    
    
    return result-1