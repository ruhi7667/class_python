# 10.Print alternate letters from the string "How are you sir"
def alternate(string):
    a=""
    for i in range(len(string)):
        if i%2==0 or string[i]==" ":
            continue
        else:
            a+=string[i]
    return a
string="How are you sir"
print(alternate(string))