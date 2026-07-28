# Search for a specific character in the string "this is python programming place"
def spe_char(string,ch):
    for i in range(len(string)):
        if string[i]==ch:
            return f"index of {ch} is :{i}"
            break
ch=input("enter the character:")
string= "this is python programming place"
print(spe_char(string,ch))