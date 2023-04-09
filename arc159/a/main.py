N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
ST = [list(map(int, input().split())) for _ in range(Q)]

class Judge:
  def __init__(self):
    self.cnt = 0

  def f(s,t):
    if (a[(s-1)%N][(t-1)%N]) == 1: return
    print(3)

for s,t in ST:
  if (a[(s-1)%N][(t-1)%N]) == 1:
    print(1)
  else:
    judge = Judge()
    judge.f(s,t)