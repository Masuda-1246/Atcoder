N, M = map(int, input().split())
while True:
  if M % N == 0:
    print(int(M/N))
    quit()
  N += 1
