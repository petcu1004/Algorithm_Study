#기초-값변환
#6025
# a, b = input().split()
# c=int(a) + int(b)
# print(c)

#6026
# a= input()
# b= input()
# c=float(a) + float(b)
# print(c)


#6027
# a=input()
# n=int(a)
# print('%x'%n) #소문자 16진수로 결과 나옴


# 6028
# a=input()
# n=int(a)
# print('%X'%n) #대문자 16진수로 결과 나옴

#6029
# a=input()
# n=int(a, 16) #입력된 a를 16진수로 인식함.
# print('%o'%n)


#6030
#ord()는 어떤 문자의 순서 위치(ordinal position)값을 의미
#문자 -> 정수값
# n=ord(input()) #입력받은 문자를 10진수 유니코드 값으로 변경
# print(n)


#6031
#chr()는 유니코드 문자(chracter)로 바꿈
#정수값 -> 문자
# c=int(input())
# print(chr(c))

#기초-산술연산
#6032
# n=int(input())
# print(-n)

#6033
# n=input() #문자로 입력 받고
# n=ord(n) #숫자로 바꾼 다음
# print(chr(n+1)) #해당 숫자에 1을 더한 뒤 다시 문자로 바꿈


#6034
# a, b=input().split()
# c=int(a)-int(b)
# print(c)

#6035
# a, b=input().split()
# c=float(a) * float(b)
# print(c)

#6036
# w, n = input().split()
# print(w * int(n))

#6037
# a=input()
# b=input()
# print(int(a) * b)

#6038
# a, b= input().split()
# c=int(a)**int(b)
# print(c)

#6039
# a, b = input().split()
# c=float(a) ** float(b)
# print(c)

#6040
# a, b = input().split()
# print(int(a)//int(b)) #믃을 출력할 때는 //을 사용

#6041
# a, b = input().split()
# print(int(a)%int(b))

#6042
# a=float(input())
# print(format(a, ".2f")) #format():반올림 된 실수 값을 만들어줌

#6043
# a, b= input().split()
# print(format(float(a)/float(b), ".3f"))

#6044
# a, b = input().split()
# c=int(a)
# d=int(b)
# print(c+d)
# print(c-d)
# print(c*d)
# print(c//d)
# print(c%d)
# print(format((c/d), ".2f"))

#6045
a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
print(a+b+c, format((a+b+c)/3, ".2f"))