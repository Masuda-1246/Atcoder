MAX_N = 1000

# 入力
N, M = map(lambda x: int(x), input().split())
G = [[] for _ in range(max(N,M)+1)]    # グラフ
print(M)
for i in range(M):
    # sからtへの辺を張る
    s, t = map(int,input().split())
    print(s)
    G[s].append(t)
    G[t].append(s)
color = [0] * N    # 頂点iの色(1 or -1)

# 頂点を1と-1で塗っていく
def dfs(v, c):
    color[v] = c    # 頂点vをcで塗る
    for i in range(len(G[v])):
        # 隣接している頂点が同じ色ならFalse
        if color[G[v][i]] == c:
            return False
        # 隣接している頂点がまだ塗られていないなら-cで塗る
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    # すべての頂点を塗れたらTrue
    return True

for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            print(0)
            exit()
print(color)
red = []
bulue = []
for i in range(len(color)):
  if color[i] == 1:
    red.append(i+1)
  else:
    bulue.append(i+1)
print(red,bulue)