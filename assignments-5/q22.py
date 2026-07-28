# 22.Check if a substring exists in "Python programming" (e.g., "thon" →Found)
def substring(string,sub):
    l=len(sub)
    for i in range(len(string)):
        if string[i:i+l]==sub:
            return "Found"
            break
    else:
        return  "Not Found"
string=input("enter your string:")
sub=input("enter your substring you want to search:")
print(substring(string,sub))