N = int(input())
A = list(map(lambda x: int(x), input().split()))
Q = int(input())
q = [list(map(lambda x: int(x), input().split())) for _ in range(Q)]
for i in range(Q):
  if q[i][0] == 1:
    A[q[i][1]-1] = q[i][2]
  else:
    print(A[q[i][1]-1])
