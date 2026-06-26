#-------tuple---------
#Defination and property of tuple
#creation of tuple
#indexing and slicing.
#TRaversing
#in-built methods
#list comprehension
#Assignment and class activity

# 1. Tuple is a data structure in python used to store multiple data of different types with comma(,) in round braces.
#2. Immutable
#3. Support indexing slicing and oredered.


#--------creation of tuple.
# t1,t2,t3=(50,40,30)
# print(type(t1))
# print(t1)
# print(t2)
# print(t3)

#indexing and slicing.
# marks_tuple=(50,55,69,34,89)
# print(marks_tuple[-1])
# print(marks_tuple[::-1])

# mutablity



#Traversing
#1. waf to extract all number greater than 55, marks_tuple=(50,55,69,34,89)
# def tuple_fun(m):
#   new_value=[]
#   for i in m:
#     if i>=55:
#       new_value.append(i)
#   return new_value
# marks_tuple=(50,55,69,34,89)
# res=tuple_fun(marks_tuple)
# print(res)

#2. waf to sum of indices of tuple marks_tuple=(50,55,69,34,89)
# marks_tuple=(50,55,69,34,89)
# s=0
# for i in range(len(marks_tuple)):
#   s+=i
# print(s)

employee_name= ["ram","rohit","rohan"]
vowels="aeiouAEIOU"
for i in employee_name:
  for j in i:
    if j in vowels:
      print(j)


# str1="this is python"
# vowels="aeiouAEIOU"
# for i in str1:
#   for j in i:
#     if j  not in vowels:
#       print(j)
      
# str1= "123ruhi456"
# digits=[]
# alpha=[]
# alnum=[]
# for i in str1:
#   if i.isdigit():
#     digits.append(i)
#   if i.isalpha():
#     alpha.append(i)
#   if i.isalnum():
#     alnum.append(i)

# print(digits)
# print(alpha)
# print(alnum)

