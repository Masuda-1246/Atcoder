N = int(input())
B = list(map(int, input().split()))
ans = [i for i in B if i%2==0]
print(*ans)