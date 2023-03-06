#6059
# n=int(input())
# print(~n)

#6060
# n, b = map(int, input().split())
# print(n&b)

#6061
# n, b = map(int, input().split())
# print(n|b)

#6062
# n, b = map(int, input().split())
# print(n^b)

#6063
# n, b= map(int, input().split())
# x=n if n>b else b
# print(x)

#6064
# n, b, c= map(int, input().split())
# x=(n if n<b else b) if ((n if n<b else b)<c) else c
# print(x)

#6065
# res = list(map(int, input().split()))

# for i in res:
#     if i % 2==0:
#         print(i)

#6066
# res = list(map(int, input().split()))
# for i in res:
#     if i % 2==0:
#         print("even")
#     else:
#         print("odd")
      
#6067
# n=int(input())

# if n<0 and n%2==0:
#     print("A")
# elif n<0 and n%2!=0:
#     print("B")
# elif n>0 and n%2==0:
#     print("C")
# elif n>0 and n%2!=0:
#     print("D")


#6068
# n=int(input())

# if n>=90 :
#   print('A')
# elif n<90 and n>=70:
#     print("B")
# elif n<70 and n>=40:
#     print("C")
# else:
#     print("D")

#6069
# n=input()

# if n=="A" :
#   print('best!!!')
# elif n=="B":
#     print("good!!")
# elif n=="C":
#     print("run!")
# elif n=="D":
#     print("slowly~")
# else:
#     print("what?")

#6070
# n=int(input())

# if n//3==1:
#     print("spring")
# elif n//3==2:
#     print("summer")
# elif n//3==3:
#     print("fall")
# else:
#     print("winter")

#6071
# n=1

# while(n!=0):
#     n=int(input())
#     if n!=0:
#         print(n)

#6072
# n=int(input())

# while(n!=0):
#     print(n)
#     n-=1

#6073
# n=int(input())

# while(n>0):
#     n-=1
#     print(n)

#6074
# c = ord(input())
# t = ord('a') #정수값으로 바꿈
# while t<=c :
#   print(chr(t), end=' ') #chr() 유니코드 문자로 바꿈
#   t += 1

#6075
# n=int(input())
# k=0
# while(k<=n):
#     print(k)
#     k+=1

#6076
n=int(input())
for i in range(n+1):
    print(i)

