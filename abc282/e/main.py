N, M = map(lambda x: int(x), input().split())
A = list(map(lambda x: int(x), input().split()))

a = []

for i in range(N):
  for j in range(i+1,N):
    a.append([i,j,(i**j+j**i)%M])
print(a)