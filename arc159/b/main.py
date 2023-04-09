from functools import lru_cache
import sys
sys.setrecursionlimit(40000)

A, B = map(int, input().split())

class GCD:
  def __init__(self):
    self.cnt = 0

  @lru_cache(maxsize=1000)
  def gcd(self,x, y):
    if y == 0:
        return x
    else:
        return self.gcd(y,x%y)

  @lru_cache(maxsize=40000)
  def f(self, a,b):
    if b == 0 or a == 0: return
    if a < b:
      tmp = a
      a = b
      b = tmp
    x = self.gcd(a,b)
    a -= x
    b -= x
    self.cnt += 1
    self.f(a,b)

  def answer(self):
    return self.cnt

gcd = GCD()
gcd.f(A,B)
print(gcd.answer())

