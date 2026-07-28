# 12.Check if the string is a palindrome (e.g., "madam" → Palindrome, "hello" → Not palindrome).
def palindrom(string):
    s=string[::-1]
    if s==string:
        return "palindrome"
    else:
        return "Not Palindrome"
string=input("enter any string:")
print(palindrom(string))