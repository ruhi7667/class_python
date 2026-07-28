# 9. Replace "python" with "javascript" in the string "python developer python engineer python holder".

def replace(string):
    l=string.split()
    l1=[]
    for i in l:
        if i=="python":
            l1.append("javascrript")
        else:
            l1.append(i)
    return " ".join(l1)
print(replace("python developer python engineer python holder"))