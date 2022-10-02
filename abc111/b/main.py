N = list(map(int, input()))
n = 0
if N[0] < N[1] or N[0] < N[2]:
  n = N[0] + 1
else:
  n = N[0] 
print(n*100+n*10+n)
  