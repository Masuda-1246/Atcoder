N =str(hex(int(input()))[2:])
N = N if len(N)==2 else f'0{N}'
print(N.upper())