# 24.Count words in the string "This is a python assignment"
def count_word(string):
    l=string.split()
    return len(l)
string=input("enter your string:")
print(count_word(string))