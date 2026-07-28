# 34.Replace a substring in "I like Python" → Replace "Python" with "Java"
def replac_sub(string,sub):
    rep=input("enter your replace string:")
    l=string.split()
    l1=[]
    for i in l:
        if i==rep:
            i=sub
            l1.append(i)
        else:
            l1.append(i)
    return " ".join(l1)
string=input("enter your string:")
sub=input("enter your substring:")
print(replac_sub(string,sub))