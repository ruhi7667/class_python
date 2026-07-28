# 14.Find the longest word in the string "Python programming is interesting"
def longest(string):
    l=string.split()
    a=[l[0]]
    for i in l:
        if len(a[-1])<len(i):
            a.append(i)
    return f"longest is:{a[-1]}"
string="Python programming is interesting"
print(longest(string))