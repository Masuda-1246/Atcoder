N = int(input())
a = set(map(int, input().split()))

l = 0
r = N+1

while r-l > 1:
  m = (r+l)//2
  c = len(set(range(1,m+1))&a)
  if c+(N-c)//2 >=m: l=m
  else: r=m

print(l)