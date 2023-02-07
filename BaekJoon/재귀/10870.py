# a=int(input())
# l=[0, 1]

# for i in range(0, a+1):
#     res=l[i]+l[i+1]
#     l.append(res)

# print(l[a])

#---------------------------------#


# a=int(input())
# l=[0, 1]

# for i in range(2, a+1):
#     l.append(l[i-2]+l[i-1])

# print(l[a])

#---------------------------------#


# n = int(input())
# l = [0,1]

# for i in range(1,n):
#     l.append(l[i]+l[i-1])
# print(l[n])


#-------------------------------------#
### 재귀
a=int(input())

def fibo(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fibo(a-2)+ fibo(a-1)

print(fibo(a))