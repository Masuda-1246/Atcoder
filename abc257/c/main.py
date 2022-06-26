N = int(input())
S = list(map(int, input()))
W = list(map(int, input().split()))
child = []
adalt = []
child_ = adalt_ = 0
for i in range(len(S)) :
  if S[i] == 0:
    child.append(W[i])
    child_ += 1
  else:
    adalt.append(W[i])
    adalt_ += 1
if child_ == 0 or adalt_ == 0:
  print(max(child_,adalt_))
  quit()
max_c = max(child)
min_a = min(adalt)
a0 = 0
a1 = 0

for a in adalt:
  if a <= max_c:
    a0 += 1
for c in child:
  if min_a <= c:
    a1 += 1
print(N-min(a0,a1))