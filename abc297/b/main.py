S = list(input())
B = []
R = []
K = 0
for i in range(len(S)):
  if S[i] == "B":
    B.append(i)
  if S[i] == "R":
    R.append(i)
  if S[i] == "K":
    K = i
print("Yes" if sum(B)%2 == 1 and R[0] < K < R[1] else "No")