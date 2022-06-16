s = input()
word_list = ["eraser", "erase", "dreamer","dream"]
for word in word_list:
  s =  s.replace(word,"")
print("YES" if(len(s)==0) else "NO")