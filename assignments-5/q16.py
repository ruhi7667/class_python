# 16.Remove all spaces from "How are you sir"
def rem_space(string):
    a=""
    for i in string:
        if i==" ":
            continue
        else:
            a+=i
    return a
string="How are you sir"
print(rem_space(string))