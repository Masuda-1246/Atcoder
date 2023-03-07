N, Q = map(lambda x: int(x), input().split())
TAB = [list(map(lambda x: int(x), input().split())) for _ in range(Q)]
ans = {(i+1):[] for i in range(N)}
for t,a,b in TAB:
  judge = b in ans[a]
  if t ==1 and not judge:
    ans[a].append(b)
  elif t==2 and judge:
    ans[a].remove(b)
  elif t==3:
    print("Yes" if (a in ans[b] and judge) else "No")