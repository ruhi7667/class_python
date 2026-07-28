# 11. Convert the string "qwertyuiopasdfghjklzxcvbnm" to "abcdefghijklmnopqrstuvwxyz"
def convert(string):
    l=list(string)
    a=sorted(l)
    return "".join(a)
print(convert("qwertyuiopasdfghjklzxcvbnm"))