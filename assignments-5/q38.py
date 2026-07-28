# 38.Check if a string ends with a substring (e.g., "Learn coding" ends with "coding")
def start_with(string,sub):
    l=string.split()
    if l[-1]==sub:
        return True
    else:
        return False
string=input("enter any string:")
sub=input("enter any substring:")
print(start_with(string,sub))