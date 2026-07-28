# 21.Remove vowels from "How are you sir" → "Hw r y sr".
def remove_vowels(string):
    a=""
    for i in string:
        if i not in "AEIOUaeiou":
            a+=i
    return a
string=input("enter any string:")
print(remove_vowels(string))