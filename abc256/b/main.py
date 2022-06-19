n = int(input())
a = list(map(int, input().split()))
score = 0
for i in range(len(a)):
  for j in range(i+1,len(a)):
    a[i]+=a[j]
  if a[i] > 3:
    score += 1
print(score)