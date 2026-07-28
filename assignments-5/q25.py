# 25.Find the ASCII value of each character in "ABcd"
def ascii_val(word):
    a=[]
    for i in word:
        a.append(ord(i))
    return a
word=input("enter your word:")
print(ascii_val(word))