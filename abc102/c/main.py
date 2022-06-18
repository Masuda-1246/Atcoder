import statistics
n = int(input())
a = list(map(int, input().split()))
b = []
ans = 0
for i in range(n):
  b.append(a[i] - i + 1)
median = statistics.median(b)
for i in range(n):
  ans += abs(b[i] - median)
print(int(ans))
