# 28.Find the first non-repeating character in "swiss" → "w"
def no_repeat(word):
    d={}
    for i in word:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if d.get(i)==1:
            return i
            break
word="swiss"
print(no_repeat(word))