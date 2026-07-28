# Remove duplicate letters from the string "this is python programming place"
def duplicate(string):
    l=list(string)
    l1=[]
    l2=[]
    for i in l:
        if i not in l2 :
            if i!=" ":
                l2.append(i)
            l1.append(i)
    return "".join(l1)
string="this is python programming place"
print(duplicate(string))
