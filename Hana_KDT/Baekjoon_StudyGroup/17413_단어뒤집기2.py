a=list(input().split(" "))

print(a)

rev=[]
origin=[]
result=[]
k=0
for i in range(len(a)):
    word=list(a[i])
    print(word)
    # for j in range(len(word)-1, 0, -1):\
    for j in range(len(word)):
        if word[j]=="<":
            if len(rev)!=0:
                for x in range(len(rev)-1, 0, -1):
                    origin.append(rev[x])
                rev=[]

            k=1
            origin.append("<")
            # continue
        elif word[j]==">":
            k=0
            origin.append(">")
            

            # continue
        elif k==0:
            rev.append(word[j])
        elif k==1:
            origin.append(word[j])
        # print(rev)
        # print(word[j])
    
    if len(rev)!=0:
            for x in range(len(rev)-1, -1, -1):
                print(rev[x])
                origin.append(rev[x])
            rev=[]
    # print(origin)
        
        
# print("".join(origin))