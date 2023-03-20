N, Q = map(int, input().split())
player = [0 for _ in range(N)]
for _ in range(Q):
  i, v = map(int, input().split())
  if i == 1:
    player[v-1] += 1
  elif i == 2:
    player[v-1] = 2
  else:
    print("Yes" if player[v-1] > 1 else "No")