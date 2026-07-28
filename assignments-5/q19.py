# 19.Swap cases of all letters in "Python Is Fun" → "pYTHON iS fUN"
def capital(string):
    l=string.split()
    l1=[]
    for i in l:
        a=""
        for j in range(len(i)):
            if j==0:
                a+=i[j].lower()
            else:
                a+=i[j].upper()
        l1.append(a)
    return " ".join(l1)
string="Python Is Fun"
print(capital(string))