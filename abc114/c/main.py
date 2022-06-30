N = int(input())

def dfs(s):
  if int(s) > N:
    return 0
  ret = 1 if all(s.count(c) for c in '753') else 0
  for c in '753':
    ret += dfs(s+c)
  return ret

print(dfs('0'))