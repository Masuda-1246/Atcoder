N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = [abs(A-(T-0.006*i)) for i in H]

print(ans.index(min(ans))+1)