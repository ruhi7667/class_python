# 33.Find all occurrences of a substring in "This is Python and Python is fun" → Substring "Python"
def  occur(string):
    l=string.split()
    d={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
string="This is Python and Python is fun"
print(occur(string))