N, K = map(int, input().split())
a = list(map(int, input().split()))
ans = sorted(a)
l = [[] for _ in range(K)]
for i,v in enumerate(a):
  l[i%K].append(v)
for v in l:
  v.sort()
b = []
for i in range(N):
  b.append(l[i%K][i//K])

print ("Yes" if ans == b else "No")