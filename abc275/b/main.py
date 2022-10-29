AF = list(map(lambda x: int(x), input().split()))
mul = AF[0]*AF[1]*AF[2]-AF[3]*AF[4]*AF[5]
print(mul%998244353)
