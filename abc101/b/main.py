n = input()
nn = list(n)
nn =list(map(int,nn))

ans = 0
for i in nn:
  ans += i
print("Yes" if(int(n)%ans==0) else "No")