# 36.Count occurrences of a substring in "banana" → Substring "ana" appears 2 times
def count_occur(string,sub):
    a=len(sub)
    count=0
    for i in range(len(string)):
        if string[i:i+a]==sub:
            count+=1
    return count
string=input("enter any string:")
sub=input("enter any substring:")
print(count_occur(string,sub))