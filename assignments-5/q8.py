# Count the total occurrences of a specific letter in the string "this is python programming place"
def count(string,ch):
    count1=0
    for i in range (len(string)):
        if string[i]==ch:
            count1+=1
    return f"occurrences of {ch} is:{count1}"
string="this is python programming place"
ch=input("enter the char name:")
print(count(string,ch))
    
        