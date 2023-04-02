N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = sorted(A+B)
ans = {i:0 for i in AB}
cnt = 1
for a in ans:
  ans[a] = cnt
  cnt+=1
tmp = []
for a in A:
  tmp.append(ans[a])
print(*tmp)
tmp = []
for b in B:
  tmp.append(ans[b])
print(*tmp)