# 37.Check if a string starts with a substring (e.g., "Python is easy" starts with  "Python")
def start_with(string,sub):
    l=string.split()
    if l[0]==sub:
        return True
    else:
        return False
string=input("enter any string:")
sub=input("enter any substring:")
print(start_with(string,sub))