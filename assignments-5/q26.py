# 26.Convert a string into a list of words using "split()" (e.g., "Python is fun" → ["Python", "is", "fun"])
def wod_split(string):
    l=string.split()
    return l
string=input("enter the string:")
print(wod_split(string))