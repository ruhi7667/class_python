# 20.Find frequency of each character in "banana" → { 'b':1, 'a':3, 'n':2 }
def frequency(word):
    d={}
    for i  in word:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
word=input("enter any word:")
print(frequency(word))