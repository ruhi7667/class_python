# 18.Sort characters alphabetically in "programming" → "aggimmnoprr"
def sor_t(word):
    a=sorted(list(word))
    return "".join(a)
word=input("enter any word:")
print(sor_t(word))