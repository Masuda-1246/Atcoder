H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
cnt=0
s=set()

def dfs(i,j,s):
  global cnt
  if A[i][j] in s:
    return
  if i == H-1 and j == W-1:
    cnt+=1
    return
  s.add(A[i][j])
  if (j+1 < W):
    dfs(i,j+1,s)
  if (i+1 < H):
    dfs(i+1,j,s)
  s.remove(A[i][j])

dfs(0,0,s)
print(cnt)