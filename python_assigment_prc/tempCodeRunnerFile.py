str1=["eat", "tea", "tan", "ate", "nat", "bat"]
li=[]
v=[]
for i in range(len(str1)):
  a=[]
  if str1[i] not in v:
    a.append(str1[i])
    v.append(str1[i])
    for j in range(i+1,len(str1)):
      if sorted (str1[i]) == sorted (str1[j]):
        a.append(str1[j])
        v.append(str1[j])
  if len(a)!=0:
    li.append(a)
print(li)




