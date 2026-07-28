# 13.Count spaces, digits, alphabets, and special characters in "Python 3.9 is awesome!!"
def ak_count(string):
    count_spa=0
    count_dig=0
    count_alpha=0
    count_spe=0
    for i in string:
        if i==" ":
            count_spa+=1
        elif i.isalpha():
            count_alpha+=1
        elif i.isdigit():
            count_dig+=1
        else:
            count_spe+=1
    return F"spaces are:{count_spa},digits are:{count_dig},alphabets are:{count_alpha} and special characters are:{count_spe}"
string=input("enter any string:")
print(ak_count(string))