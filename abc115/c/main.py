N, K = map(int, input().split())
H = [int(input()) for _ in range(int(N))]
H.sort()
h_min = 10**10
for i in range(N - K + 1):
  h_min = min(h_min,abs(H[i+K-1] - H[i]))
print(h_min)

