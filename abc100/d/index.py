N, M = map(int, input().split())
xyzs = [tuple(map(int, input().split())) for _ in range(N)]
 
ans = 0
for S in range(1<<3):
    signs = []
    for i in range(3):
        if (S>>i)&1:
            signs.append(1)
        else:
            signs.append(-1)
    a, b, c = signs
    vs = []
    for x, y, z in xyzs:
        v = a*x + b*y + c*z
        vs.append(v)
    vs.sort(reverse=True)
    sm = sum(vs[:M])
    if sm > ans:
        ans = sm
 
print(ans)