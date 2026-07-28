# 1. Filter vowels and consonants from the string "How are you sir".
def vol_con(string):
    str1=""
    str2=""
    for i in string:
        if not i.isalpha():
            continue
        elif i in "AEIOUaeiou":
            str1+=i
        else:
            str2+=i
    return f"vowels are:{str1} and consonants are:{str2}"
string= "How are you @sir"
print(vol_con(string))