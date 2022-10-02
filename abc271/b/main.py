N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(int(N))]
Q = [list(map(int, input().split())) for _ in range(int(Q))]
sorted(A, key=lambda x: x[1])
for s,t in Q:
  print(A[int(s)-1][t])