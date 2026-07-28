# 45.Find the longest common substring between two strings (e.g., "abcdxyz" and "xyzabcd" → Longest common substring = "abcd").
def longest(str1,str2):
    l=[""]
    for i in range(len(str1)):
        for j in range(len(str1)):
            if str1[i:j] in str2:
                if len(l[-1])<len(str1[i:j]):
                    l.append(str1[i:j])
    return f"longest common substring is:{l[-1]}"
str1=input("enter string1:")
str2=input("enter string2:")
print(longest(str1,str2))