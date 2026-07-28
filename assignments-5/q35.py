# 35.Remove a substring from "HelloWorld" → Remove "World" → "Hello".
def rem_sub(string,sub):
    a=len(sub)
    for i in range(len(string)):
        if string[i:i+a]==sub:
            b=i
            break
    ans=""
    for i  in range(0,b):
        ans+=string[i]
    return ans
string=input("enter any string:")
sub=input("enter any substring:")
print(rem_sub(string,sub))