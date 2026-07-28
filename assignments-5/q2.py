# 2. Count vowels and consonants in the string "How are you sir"
def vol_con(string):
    count1=0
    count2=0
    for i in string:
        if not i.isalpha():
            continue
        elif i in "AEIOUaeiou":
            count1+=1
        else:
            count2+=1
    return f"no of vowels are:{count1} and no of consonants are:{count2}"
string= "How are you @sir"
print(vol_con(string))