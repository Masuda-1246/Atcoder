n, m = map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(int(m))]

ab = sorted(ab, key = lambda x:x[1])
r = ab[0][1]
cnt = 1
for i in range(m):
  if ab[i][0] >= r:
    cnt += 1
    r = ab[i][1]
print(cnt)