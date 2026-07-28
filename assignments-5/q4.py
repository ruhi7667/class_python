# 4. Convert lowercase letters to uppercase in the string "How are you sir"
def con_lower(string):
    s=""
    for i in string:
        if i.islower():
            a=i.upper()
            s+=a
        else:
            s+=i
    return s
string="How are you sir"
print(con_lower(string))