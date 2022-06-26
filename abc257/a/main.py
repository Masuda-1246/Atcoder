N, X = map(int, input().split())
word = [chr(ord("A")+i) for i in range(26)]
print(word[X//N-1] if X%N == 0 else word[X//N])