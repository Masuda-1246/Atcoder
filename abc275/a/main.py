from operator import indexOf


N = input()
H = list(map(lambda x: int(x), input().split()))
print(H.index(max(H))+1)