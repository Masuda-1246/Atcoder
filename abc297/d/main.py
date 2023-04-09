A, B = map(int, input().split())
cnt = 0
while A!=B:
  if A>B:
    if A%B == 0:
      cnt += A//B-1
      break
    cnt += A//B
    A%=B
  else:
    if B%A == 0:
      cnt += B//A-1
      break
    cnt += B//A
    B%=A
print(cnt)