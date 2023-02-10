#최소직사각형

def solution(sizes):

    a=[]
    b=[]
    
    for i in range(len(sizes)):
        if sizes[i][0]<=sizes[i][1]:
            res=sizes[i][0]
            sizes[i][0]=sizes[i][1]
            sizes[i][1]=res
            
        a.append(sizes[i][0])
        b.append(sizes[i][1])
    # print(sizes)
    a.sort(reverse=1)
    b.sort(reverse=1)
    return a[0]*b[0]


    #------------------------------#
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col