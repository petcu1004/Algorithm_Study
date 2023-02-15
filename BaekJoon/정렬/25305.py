# 커트라인

a, b=map(int, input().split())
l=list(map(int, input().split()))

l.sort(reverse=1)

print(l[b-1])
