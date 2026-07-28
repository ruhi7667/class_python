# 43.Extract substring before a specific word (e.g., "Welcome to Python World" → substring before "Python" → "Welcome to").
def akash(string,sub):
    l=string.split()
    a=0
    for i in range(len(l)):
        if l[i]==sub:
            a=i
            break
    l1=l[:a]
    return " ".join(l1)

string=input("enter your string:")
sub=input("enter your substring:")
print(akash(string,sub))