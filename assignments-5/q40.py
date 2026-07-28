# 40.Find the index of the first occurrence of a substring in "Programming is great" → Substring "is" → Index 12
def index(string,sub):
    l=string.split()
    a=0
    for i in range(len(l)):
        if l[i]==sub:
            a=i
            break
    count=0
    for j in range(a-1,-1,-1):
        count+=len(l[j])
    return f"index is:{count+a}"
string=input("enter the string:")
sub=input("enter the substring:")
print(index(string,sub))

# s="Programming is great"
# s1="is"
# c=len(s1)
# for i in range(len(s)):
#     for j in range(len(s1)):
#         if s[i]==s1[j]:
#             i=i+1
#             j=j+1
#         else:
#             i=i+1
#     if c==j:
#         print("index:",i-c)
#         break
# for i in range(1,11):
#     print(i)
    