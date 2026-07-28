# 15.Capitalize the first letter of each word in "welcome to python world"
def capital(string):
    l=string.split()
    l1=[]
    for i in l:
        a=""
        for j in range(len(i)):
            if j==0:
                a+=i[j].upper()
            else:
                a+=i[j]
        l1.append(a)
    return " ".join(l1)
string="welcome to python world"
print(capital(string))