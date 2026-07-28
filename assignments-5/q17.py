# 17.Check if all characters in the string are unique (e.g., "abcde" → True "hello" → False).
def unique(string):
    l=[]
    for i in string:
        if i not in l:
            l.append(i)
        else:
            return False
    return True
string=input("enter any string:")
print(unique(string))