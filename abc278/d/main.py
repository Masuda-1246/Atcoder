N = int(input())
A = list(map(lambda x: int(x), input().split()))
Q = int(input())
query = [list(map(lambda x: int(x), input().split())) for _ in range(Q)]

last = 0
for i in range(len(query)):
  if query[i][0] == 3:
    last = i
query = query[:last+1]
for q in query:
  if q[0] == 1:
    A = [q[1] for _ in range(N)]
  elif q[0] == 2:
    A[q[1]-1] += q[2]
  elif q[0] == 3:
    print(A[q[1]-1])