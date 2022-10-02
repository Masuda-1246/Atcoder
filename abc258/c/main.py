N, Q  = map(int, input().split())
S = list(input())
query = [list(map(int, input().split())) for _ in range(Q)]
for t, x in query:
  if t == 1:
    S = S[N-x:]+S[0:(N-x)]
  elif t == 2:
    print(S[x-1])