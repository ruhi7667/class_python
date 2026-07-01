#conditional statements
 #single line if/ Ternary operator
# food=input("food: ")
# eat = "Yes" if food == "cake" else "no"
# print(eat)

# food = input("food : ")
# print("sweet") if food == "cake" or food=="jalebi" else print("not sweet")

#clever if/Ternary Operator
# age = int(input("age :" ))
# vote = ("yes", "no") [age<18]
# light=input("Enter light color:"  )
# if (light == "Red"):
#   print("stop")
# elif (light == "Green"):
#   print("Go")
# elif (light == "Yellow"):
#   print("lookout")
# else:
#     print("Your light is broken ")

# str1=["python programming"]
# rev=str1[0][::-1]
# print(rev)

# str1=["python programming"]
# s=''  
# for i in str1:
#   s+=i
# l=[i for i in s]
# temp=l[0]
# l[0]=l[-1]
# l[-1]=temp
# res="".join(l)
# print(res)
#slicing
"""str ="Apple"
print(str[-5:len(str)])"""

# str="i am studying python for DataScience"
# print(str.endswith("ce"))
# str = str.capitalize()
# print(str)
# print(str.replace("python","machine learning"))
# print(str.find("for"))
# print(str.count("o"))

# name=(input("Enter User First Name"))
# for i in range (len(name)):
#   print(i)
# str=" Hii $I am the $ symbol $99.99 "
# print(str.count("$"))

# marks =int(input("Enter your marks"))
# if (marks >= 90):
#   print("grade A")
# elif (marks >=80  and marks < 90):
#   print("grade B")
# elif (marks >= 70 and marks < 80):
#   print("grade C")
# elif (marks < 70 and marks >= 50):
#   print("grade D")
# else:
#   print("Fail")

# num = int(input("Enter a Number"))
# if num % 2 ==0:
#   print("num is even")
# else:
#   print("num is odd")

# num1 =int(input("Enter Your First No:"))
# num2 =int(input("Enter Your Second No:"))
# num3 = int(input("Enter Your Third No:"))
# if(num1 > num2 and num1 > num3):
#   print("num1 is greatest num:", num1)
# elif(num2 > num3 and num2 > num1):
#   print("num2 is greatest num:", num2)
# else:
#   print("num3 is greatest num", num3)

# num = int(input("Enter a number"))
# if (num % 7 == 0):
#   print("num is multiple of 7")
# else:
#   print("num is not multiple of 7")

#list 
#in list we can store elements of different type (integer, float string, etc.)

#  marks=[94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))

# list1=[77, 75,44,47, 89,88,81]
# list1.reverse()
# print(list1)

# list=[8,78,98,0,56,65]
# list.append(4)
# list.sort()
# list.sort(reverse=True)
# list.reverse()
# list.insert(1,66)

# list =["I am Ruhi", "She is my Friend", "Her name is Shivani"]
# list.sort( reverse = True)
# print(list)

# list = [66, 44, 35, 20]
# print (list.remove(44))
# list.pop(2)


#----tuples
# tup=(2, 1, 3, 1)
# print(type(tup[0]))
# print(tup.index(3))
# print(tup.count(2))

# movie_name_1st = input("Enter your First Movie Name")
# movie_name_2nd = input("Enter your Second Movie Name")
# movie_name_3rd = input("Enter your third Movie Name")
# list=[]
# list.append(movie_name_1st)
# list.append(movie_name_2nd)
# list.append(movie_name_3rd)
# print(list)

# movies=[]
# movies.append(input("Enter 1st movie:"))
# movies.append(input("Enter 2nd movie:"))
# movies.append(input("Enter 3rd movie:"))
# print (movies)

# list1=[1,2,1]
# list2=[1,2,3]
# copy_list1=list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1):
#   print("yes this is palindrome")
# else:
#   print("not palindrome")

# grade = ["C", "D", "B", "A", "C", "B","B","A"]
# print(grade.count("A"))
# grade.sort()
# print(grade)

#-----dictionary
dict={
  "name" :" Ruhi",
  "address":["Abhaipur", "Noida", "Delhi","Udaipur"],
  "age": 23,
  "is_adult": True,
  "marks": 89.9
}
dict["Surname"] = "Singh"
print(dict["Surname"])











 
 