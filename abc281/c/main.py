S,T = map(lambda x: int(x), input().split())
A = list(map(lambda x: int(x), input().split()))
T %= sum(A)
for i in range(len(A)):
  if T < A[i]:
    break
  T -= A[i]
print(i+1,T)