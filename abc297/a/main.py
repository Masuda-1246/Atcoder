N, D = map(int, input().split())
T = list(map(int, input().split()))

t1 = T[0]

for i in range(1, N):
  if T[i] - t1 <= D:
    print(T[i])
    exit()
  else:
    t1 = T[i]
print(-1)