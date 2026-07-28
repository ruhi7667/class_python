# 30.Replace all spaces with hyphens (-) in "Python is easy to learn" →"Python-is-easy-to-learn"
def space_hyphens(string):
    l=string.split()
    return "-".join(l)
string=input("enter the string:")
print(space_hyphens(string))