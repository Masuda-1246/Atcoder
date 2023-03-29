N = int(input())
A = list(map(int, input().split()))
ans = 0
socks = {i:0 for i in A}

for a in A:
  socks[a] += 1

for a in socks:
  ans += socks[a] // 2

print(ans)