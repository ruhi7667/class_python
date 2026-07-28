# 32.Check if one string is a substring of another (e.g., "gram" is a substring of "Programming")
def sub_string(string,sub):
    a=len(sub)
    for i in range(len(string)):
        if string[i:i+a] in string:
            return True
            break
    else:
        return False
string=input("enter your string:")
sub=input("enter your substing:")
print(sub_string(string,sub))