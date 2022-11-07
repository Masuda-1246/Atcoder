from functools import lru_cache

# N = int(input())
# A = list(map(lambda x: int(x), input().split()))
N = 3
A = [36, 1, 36]

cnt = 0
c2 = []
c3 = []

for i in range(N):
  a = A[i]
  cnt2=0
  cnt3=0
  while a%2==0:
    a/=2
    cnt2+=1
  while a%3==0:
    a/=3
    cnt3+=1
  if a>5:
    print(-1)
    quit()
  c2.append(cnt2)
  c3.append(cnt3)
min2 = min(c2)
min3 = min(c3)
sum2 = sum(c2) - min2*N
sum3 = sum(c3) - min3*N
print(sum2+sum3)