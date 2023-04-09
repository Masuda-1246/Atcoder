N ,K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

index = 1
init_cost = A[0]
cost = init_cost
cnt = 0

while True:
  if cnt == K: break
  init_cost+=1
  

print(cost)