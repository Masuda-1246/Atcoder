N, M = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(int(M))]
PYC = PY.copy()
PYC.sort()
p_old = 1
cnt = 0
ans = {y:"" for p, y in PY}
for p, y in PYC:
  if p == p_old:
    cnt += 1
  else:
    p_old = p
    cnt = 1
  s = "0"*(6-len(str(p))) + str(p) + "0"*(6-len(str(cnt))) + str(cnt)
  ans[y] = s

for p, y in PY:
  print(ans[y])