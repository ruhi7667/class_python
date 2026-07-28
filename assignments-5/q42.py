# 42.Extract substring after a specific word (e.g., "Welcome to Python World" → substring after "to" → "Python World").
def akash(string,sub):
    l=string.split()
    a=0
    for i in range(len(l)):
        if l[i]==sub:
            a=i
            break
    l1=l[a+1:]
    return " ".join(l1)

string=input("enter your string:")
sub=input("enter your substring:")
print(akash(string,sub))
