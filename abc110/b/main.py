N, M, X, Y = map(int,input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for a in range(X+1,Y+1):
  if (max(x)<a and a <= min(y)):
    print("No War")
    quit()
print("War")

