# 44.Check if two strings are rotations (cyclic substrings) of each other (e.g., "abcd" and "cdab" → Rotations).
def rotations(str1,str2):
    a=str1*2
    if len(str1)!=len(str2):
        return "not Rotations"
    if str2 in a:
        return "rotations"
    else:
        return "not rotations"

str1=input("enter string1:")
str2=input("enter string2:")
print(rotations(str1,str2))