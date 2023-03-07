H, M = input().split()
def f(a,b):
  A,B,C,D = 0,0,0,0
  if len(a) > 1:
    A = a[0]
    B = a[1]
  else:
    B = a[0]
  if len(b) > 1:
    C = b[0]
    D = b[1]
  else:
    D = b[0]
  h = int(str(A)+str(C))
  m = int(str(B)+str(D))
  if h<24 and m<59:
    print(a, b)
  else:
    a = int(a)
    b = int(b)
    f(str(a+((b+1)//60)),str((b+1)%60))
f(H,M)