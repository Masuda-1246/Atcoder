N = int(input())
P = [int(input()) for _ in range(int(N))]
P.sort()
P[-1] = P[-1] // 2
print(sum(P))