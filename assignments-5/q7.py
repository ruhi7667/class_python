# 7. Find the greatest and smallest characters from the string "venugopaliyer"
def greatest_char(string):
    gar=string[0]
    for i in string:
        if i>gar:
            gar=i
    return f"greatest character are:{gar}"
string="venugopaliyer"
print(greatest_char(string))