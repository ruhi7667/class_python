# 41.Find the index of the last occurrence of a substring in "Programming in Python Programming" → Substring "Programming".

def index(string,sub):
    l=string.split()
    a=0
    for i in range(len(l)-1,-1,-1):
        if l[i]==sub:
            a=i
            break
    count=0
    for j in range(a-1,-1,-1):
        count+=len(l[j])
    return f"index is:{count+a}"
string=input("enter the string:")
sub=input("enter the substring:")
print(index(string,sub))