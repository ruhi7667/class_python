# 29.Check if two strings are anagrams (e.g., "listen" and "silent" →Anagrams)
def anagram(string1,sring2):
    if sorted(string2)==sorted(string1):
        return "Anagram"
    else:
        return "Not anagrams"
string1=input("enter the fist string:")
string2=input("enter the second string:")
print(anagram(string1,string2))

# alternate method
str1="listen"
str2="silent"
for i in str1:
    if i  not in str2:
        print("Not Anagram")
        break
else:
    print("anagram")