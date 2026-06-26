# 1. Write a Python program to find the sum of all elements in the list [10, 20, 30,  40, 50].

# all_element=[10,20,30,40,50]
# total=sum(all_element)
# print("sum of all element:", total)

#2.Write a Python program to display the odd and even elements from the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

# list = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# print("Even elements")
# for i in list:
#   if i % 2 == 0:
#     print(i, end=" ")
    
# print("\nOdd elements:")
# for i in list:
#   if i % 2 !=0:
#     print(i, end=" ")
    
#3.Write a Python program to count the odd and even numbers in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

# lis=[10, 23, 11, 12, 33, 44, 2, 5, 6]
# even_count=0
# odd_count=0
# for i in lis:
#    if i % 2 == 0:
#      even_count += 1
#    else:
#      odd_count += 1
  
# print("Even Numbers Count:", even_count )
# print("Odd Numbers Count:", odd_count)
 
#4.Write a Python program to interchange the first and last elements in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].
# list = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# first_elm=list[0]
# last_elm=list[-1]
# list[0]= last_elm
# list[-1]=first_elm
# print(list)

#5. Write a Python program to duplicate all the items in the list li = [1, 2, 3], 
# such that the result is: 
# output = [1, 2, 3, 1, 2, 3, 1, 2, 3]. 
# list=[1,2,3]
# res=list*3
# print(res)

#6.Find the smallest element in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].
# list=[10, 23, 11, 12, 33, 44, 2, 5, 6]

# smallest_number=list[0]
# for i in list:
#   if i < smallest_number:
#     smallest_number = i
    
# print("Smallest Number:" , smallest_number )
 
#7.  Find the greatest element in the list [89, 23, 24, 2, 55, 54, 64].  
# list=[89, 23, 24, 2, 55, 54, 64]
# greatest_num=list[0] 
# for i in list:
#   if i >greatest_num:
#     greatest_num = i
# print("Greatest Number:", greatest_num)
  
#8. Find the repetitive elements in the list [1,2,3,4,56,1,22,23,33,23, 56].

# li = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# seen = set()
# duplicates = set()

# for i in li:
#     if i in seen:
#         duplicates.add(i)
#     else:
#         seen.add(i)

# print("Repetitive elements:", list(duplicates))

#9. Remove all the odd elements from the list [10, 23, 11,12,33,44,2,5, 6].

# list = [10,23,11,12,33,44,2,5,6]
# result=[]
# for i in list:
#   if i % 2 == 0:
#     result.append(i)
# print("Remove odd elements:", result)

#10. Find all non-repetitive elements in the list[1,2,3,4,56,1,22,23,33,23,56]
# list = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# result=[]
# for i in list:
#   if list.count(i) ==1:
#     result.append(i)

# print("Non-repetitive elements:", result)

#11.Write a Python program to duplicate all items in the list l = [1, 2, 3] to produce the result: 
#result = [1, 2, 3, 1, 2, 3, 1, 2, 3]

# l = [1, 2, 3] 
# result=l*3
# print(result)

# l=[1,2,3]
# result=[]
# for i in range(2):
#   result.extend(l)
# print(result)
#12. Find the second greatest element in the list [89, 23, 24, 2, 55, 54, 64]

# list=[89,23,24,2,55,54,64]
# greatest_ele=list[0]
# for i in list:
#   if i > greatest_ele:
#     greatest_ele = i
# print(greatest_ele)
# list.sort(reverse=True)
# print(list)
# print(list[1])
#  13. Reverse the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56].
# list= [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# list.reverse()
# print(list)
#Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in ascending order. 

# list =[1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] 
# list.sort()
# print(list)
# 15.list.sort(reverse=True)
# print(list)
#16.Write a Python program to print all the vowels present in the given list of strings ["Dreamer", "infotech"]. 
# str1=["Dreamer","infotech"]
# vowel="aeiouAEIOU"
# for i in str1:
#   for j in i:
#     if j in vowel:
#       print(j)
# 17. Write a Python program to take input from the user to create a list of elements. 
# The user should input each element of the list one by one. Create a list with these elements (maximum of 5 elements). 
# elements =[]
# for i in range(5):
#   item = int(input(f"Enter element {i+1}:"))
#   elements.append(item)
# print("List created:",elements)
#18. Write a Python program to generate a list of numbers in reverse order from 10 to 1 using list comprehension.
# numbers = [i for i in range(10,0,-1)]
# print(numbers)

# 19. Create a list of square numbers from 1 to 10 using list comprehension. 
# square_numbers= [i**2 for i in range(1,11)]
# print(square_numbers)
#20.Create a list of even numbers from 1 to 10 using list comprehension.
# even_numbers=[i for i in range(1,11) if i % 2 == 0]
# print(even_numbers)
#21.  Filter strings from the list language = ['python', 'php', 'java', 'c++', 'javascript', 'ruby'] that contain a specific letter provided by the user, using list comprehension.
# language = ['python', 'php', 'java', 'c++', 'javascript', 'ruby']

# letter = input("Enter a letter: ")

# result = [i for i in language if letter.lower() in i.lower()]

# print("Matching languages:", result)

#22.. Flatten a nested list like [[1,2], [3,4], [5,6]] into a single list. 
# nested_list = [[1, 2], [3, 4], [5, 6]]
# flat_list =[num for sublist in nested_list for num in sublist]
# flat_list = []
# for sublist in nested_list:
#     for num in sublist:
#         flat_list.append(num)
# print(flat_list)
# 23. Find the frequency of each element in a list.  List:  [1, 2, 2, 3, 4, 1, 5, 2] 
# Output: 
# 1 → 2 times 
# 2 → 3 times 
# 3 → 1 times
# li= [1, 2, 2, 3, 4, 1, 5, 2]
# frequency = {}
# for i in li:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1

# for key, value in frequency.items():
#     print(key, "→", value, "times")

# 24.Check whether a given list is a palindrome. 
# List: 
# [1, 2, 3, 2, 1] 
# Output: 
# Palindrome

# List = [1, 2, 3, 2, 1] 
# if List == List[::-1]:
#   print("palindrome")
# else:
#   print("Not palindrome")

# 25. Find the longest string in a list of strings.   
# List:["cat", "elephant", "dog", "hippopotamus"] 
# Output: "hippopotamus" 
# li=["cat", "elephant", "dog", "hippopotamus"] 
# longest_str=li[0]
# for i in li:
#   if i > longest_str:
#    longest_str = i
# print(longest_str)

#26.. Count how many strings in a list start with a vowel. 
# List:  ["apple", "banana", "orange", "umbrella", "grape", "ice"] 
# Output:  4 strings start with a vowel(apple, orange, umbrella, ice) 

# List= ["apple", "banana", "orange", "umbrella", "grape", "ice"]
# vowel="aeiouAEIOU"
# count=0
# for i in List:
#   if i[0].lower() in vowel:
#         count += 1
#         print(i)

# print("count:",count)

#27.  Replace all negative numbers in a list with zero 
# List: [5, -3, 7, -1, 0, -8, 4]
# List= [5, -3, 7, -1, 0, -8, 4]
# res =[]
# for i in range(len(List)):
#   List[i]=abs(List[i]) 
# print(List)

#28.Create a new list containing only prime numbers from a given list. 
# list1=[2,3,4,5,6,7,8,9]
# prime_num=[]
# for i in list1:
#   if i > 1:
#     is_prime = True

#     for j in range(2,i):

#       if  i%j == 0:
#         is_prime = False
#         break
    
#     if is_prime:
#       prime_num.append(i)

# print("Prime Numbers:", prime_num)

#29.Convert a list of integers into a single integer number (e.g., [1,2,3,4] → 1234). 

# list1 =[1,2,3,4,5,6,7,8,9]
# num=int("".join(map(str,list1)))
# print(num)

# 30. Group elements of a list based on even and odd indices.
# num=[10,20,25,15,30,35,33,32,23,11]
# even_num=[]
# odd_num=[]
# for i in range(len(num)):
#   if i % 2 == 0:
#     even_num.append(num[i])
#   else:
#     odd_num.append(num[i])

# print("Even Index",even_num)
# print("Odd Index",odd_num)

 #31.Find the largest even number in a list.
# num=[90,20,25,15,30,35,33,32,23,11]
# largest_even_num=num[0]
# for i in  num:
#   if i % 2 == 0:
#      if i > largest_even_num:
#             largest_even_num = i
# print(largest_even_num)

# 32. Find the majority element in a list (an element that appears more than n/2 times). List:[2, 2, 1, 2, 3, 2, 2]   
# li=[2, 2, 1, 2, 3, 2, 2] 
# list1=[]
# a=len(li)
# for i in range(len(li)):
#   count=1
#   if li[i] not in list1:
#     for j in range(i+1,len(li)):
#       if li[i] ==li[j]:
#         count+=1
#     li.append(li[i])
#   if count>=a//2:
#     print(li[i])

#33. Find the difference between the maximum and minimum values in a list.
# list1=[10, 4, 7, 2, 15, 6]
# a=max(list1)
# b=min(list1)
# print(a-b)

#34. Remove every third element from a list.
# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([i for i in range(len(list1))if i % 3!=0])

#35. Insert an element at every even index of a list.
# list1=[1, 2, 3]
# n=int(input("enter an ele :"))
# for i in range(len(list1)):
#   if i % 2 ==0:
#     list1.insert(i,n)
# print(list1)

#36.Rearrange a list so that positive and negative numbers alternate

# list1=[1, 2, 3, 4, -3, -4, -5,-6]
# l1=[]
# l2=[]
# for i in list1:
#   if i>0:
#     l1.append(i)
#   else:
#     l2.append(i)
# res=[]
# i=0
# j=0
# while(i<len(l1) and j<len(l2)):
#   res.append(l1[i])
#   res.append(l2[j])
#   i+=1
#   j+=1
# print(res)

#37..Find all pairs of elements in a list whose sum equals a given target number.
# list1=[1, 2, 3, 4, 5, 6]
# target_num=int(input("enter a target number:"))
# for i in range(len(list1)):
#   for j in range(i+1,len(list1)):
#     if list1[i] +list1[j]==target_num:
#       print(list1[i],list1[j])

# 38.Find the Missing Number from a Sequence.

# list1=[1, 2, 4, 5, 6]
# a=max(list1)
# b=min(list1)
# for i in range(b,a+1):
#   if i not in list1:
#     print(i,end=" ")

# 39.Split a List into Chunks of Size 3
# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# li=[list1[i:i+3] for i in range(0,len(list1),3)]
# print(li)

#40. Reverse Each String in a List.
# list1=["python", "java", "script"]
# li=[]
# for i in list1:
#   li.append(i[::-1])
#   print(li)

#41.Extract All Digits from a List of Strings
# list1=["abc123", "45def","gh67"]
# li=[]
# for i in list1:
#   a=''
#   for j in i:
#     if j.isdigit():
#       a+=j
#   li.append(a)
# print(li)

#42.Find All Anagram Groups in a List of Words
# str1=["eat", "tea", "tan", "ate", "nat", "bat"]
# li=[]
# v=[]
# for i in range(len(str1)):
#   a=[]
#   if str1[i] not in v:
#     a.append(str1[i])
#     v.append(str1[i])
#     for j in range(i+1,len(str1)):
#       if sorted (str1[i]) == sorted (str1[j]):
#         a.append(str1[j])
#         v.append(str1[j])
#   if len(a)!=0:
#     li.append(a)
# print(li)




