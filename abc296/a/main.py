N = int(input())
S = list(input())
tmp = S[0]
for i in range(1, N):
  if tmp == S[i]:
    print("No")
    exit()
  tmp = S[i]
print("Yes")
