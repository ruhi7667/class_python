#1. Write a program to calculate the sum of all keys in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4} 
# d = {1: 1, 2: 2, 3: 3, 4: 4} 
# sum=0
# for key in d.keys():
#   sum +=key
# print("Sum of all keys:",sum)

# 2.Write a program to calculate the sum of all values in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4} 
# d = {1: 1, 2: 2, 3: 3, 4: 4} 
# sum=0
# for value in d.values():
#   sum +=value
# print("Sum of all values:",sum )

#3. Write a program to calculate the sum of both keys and values in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4} 
# d = {1: 1, 2: 2, 3: 3, 4: 4} 
# total=0
# sum=0
# for key in d.keys():
#   total+=key
# print("Sum of all keys:",total)
# for value in d.values():
#   sum +=value
# print("Sum of all Values:",sum)

# 4. Create an empty dictionary called user_data. 
# Allow the user to enter key-value pairs until they choose to stop. Print the final dictionary. 
# user_data={}
# while True:
#     key = input("Enter key: ")
#     value = input("Enter value: ")

#     user_data[key] = value

#     choice = input("Do you want to add more? (yes/no): ")

#     if choice.lower() == "no":
#         break

# print("Final Dictionary:")
# print(user_data)

# 5. Write a program to calculate the total score of all students 
# student_score = {1: 44, 2: 45, 3: 55} 
# student_score = {1: 44, 2: 45, 3: 55}
# total_score=0
# for i in student_score.values():
#   total_score +=i
# print("Total Score :", total_score)

# 6. Write a program to separate odd and even keys from a dictionary. 
# Also count the total number of odd keys and even keys. 
# odd_even={1:21, 2: 43, 3:41, 4:32, 5:31, 6:30}
# odd_key_no={}
# even_key_no={}
# for key in odd_even.keys():
#   if key % 2 ==0:
#     even_key_no[key] = odd_even[key]
#   else:
#     odd_key_no[key] = odd_even[key]

# print("Odd keys:", odd_key_no)
# print("Even keys:", even_key_no)

# print("odd keys no", len(odd_key_no))
# print("even keys no",len(even_key_no))

# 7. Write a program to find the greatest key in the dictionary 
# player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"} 

# player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"} 
# greatest_key=0
# for key in player:
#   if key > greatest_key:
#     greatest_key=key
# print("Greatest Key:", greatest_key)
# print("player Name:", player[greatest_key])

# 8. Write a program to extract alternate key-value pairs from the dictionary 
# player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"} 

# def laternate(d):
#     ans={}
#     l=[]
#     l1=[]
#     for i in d:
#         l.append(i)
#         l1.append(d.get(i))
#     for j in range(len(l)):
#         if j%2==0:
#             ans[l[j]]=l1[j]
#     return ans
# player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
# # print(len(player))
# print(laternate(player))

# 9. Write a program to find all values that start with the letter ‘K’
# def letter_with_K(d):
#     l=[]
#     for i in d:
#         a=d.get(i)
#         if a[0]=="K":
#             l.append(d.get(i))
#     return l
# player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
# print(letter_with_K(player))

# 10. Write a program to merge two dictionaries
# def merge(d1,d2):
#     for i  in d2:
#         d1[i]=d2.get(i)
#     return d1
# d1 = {1: "a", 2: "b"}
# d2 = {3: "c", 4: "d"}
# print(merge(d1,d2))

# 11. Write a program to check whether a given key exists in the dictionary
# def exit(d,key):
#     for i in d:
#         if i==key:
#             return "key exists"
#     else:
#         return "key not exists"
# d = {1: 100, 2: 200, 3: 300, 4:450, 5:250}
# key=int(input("enter key:"))
# print(exit(d,key))

# 12. Write a program to find the minimum value in the dictionary
# def mini_value(d):
#     mini=100
#     for i in d:
#         if d.get(i)<mini:
#             mini=d.get(i)
#     return f"minimum value in the dictionary:{mini}"
# marks = {"A": 85, "B": 90, "C": 75, "D": 95}
# print(mini_value(marks))

# 13. Write a program to find the maximum value in the dictionary
# def max_value(d):
#     max=-100
    
#     for i in d:
#         if d.get(i)>max:
#             maxi=d.get(i)
#     return f"maximum value in the dictionary:{max}"
# marks = {"A": 85, "B": 90, "C": 75, "D": 95}
# print(max_value(marks))

# 14. Write a program to swap keys and values in the dictionary
# def swap_key_val(d):
#     new_d={}
#     for i  in d:
#         new_d[d.get(i)]=i
#     return new_d
# d = {1: "one", 2: "two", 3: "three"}
# print(swap_key_val(d))

#  15. Write a program to remove a specific key (for example, key = 2) from the dictionary
# def rem(d,key):
#     d1={}
#     for i in d:
#         if i==key:
#             continue
#         else:
#             d1[i]=d.get(i)
#     return d1
# d = {1: 10, 2: 20, 3: 30}
# print(rem(d,2))

# 16. Write a program to count the frequency of each character in a string using a dictionary. Example: "banana"
# def freq(word):
#     d={}
#     for i in word:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     return d
# print(freq("banana"))

# 17. Write a program to create a dictionary where keys are numbers from 1 to 5 and values are their squares.
# def create_dic():
#     d={}
#     for i  in range(1,6):
#         d[i]=i*i
#     return d
# print(create_dic())

# 18. Write a program to find the total number of items in the dictionary
# def total(d): 
#     count=0
#     for i  in d:
#         count+=1
#     return count
# d = {"apple": 5, "banana": 7, "cherry": 3}
# print(total(d))

# 19. Write a program to sort a dictionary by its keys
# def sort(d):
#     return dict(sorted(d.items()))
# d = {3: "three", 1: "one", 2: "two"}
# print(sort(d))

# 20. Write a program to count how many values are greater than 50 in a dictionary.
# def cal(d):
#     count=0
#     for i in d:
#         if d.get(i)>50:
#             count+=1
#     return count
# d = {1: 10, 2: 20, 3: 30,4:90,5:56,6:23,7:100}
# print(cal(d))

# 21. Write a program to find the key with the highest value in a dictionary
# def max_value(d):
#     max=-100
#     l=[]
#     for i in d:
#         if d.get(i)>max:
#             maxi=d.get(i)
#             l.append(i)
#     return f"key with maximum value in the dictionary:{l[-1]}"
# marks = {"A": 85, "B": 90, "C": 75, "D": 95}
# print(max_value(marks))

# 22. Write a program to update a value in a dictionary if the key exists; otherwise, add the key.
# def exit(d,key,val):
#     for i in d:
#         if i==key:
#             d[i]=val
#             break
#     else:
#         d[key]=val
#     return d
# key=int(input("enter key:"))
# val=int(input("enter val:"))
# d = {1: 10, 2: 20, 3: 43,4:90,5:65,6:23,7:100,8:99, 9:55}
# print(exit(d,key,val))

# 23. Write a program to convert two lists into a dictionary Example: keys = [1, 2, 3], values = ["a", "b", "c"]
# def list_dict(keys,values):
#     d={}
#     for i in range(len(keys)):
#         d[keys[i]]=values[i]
#     return d
# keys=[1, 2, 3]
# values=["a", "b", "c"]
# print(list_dict(keys,values))

# 24. Write a program to remove duplicate values from a dictionary
# def dupli(d):
#     d1={}
#     l=[]
#     for i in d:
#         if d.get(i) not in l:
#             l.append(d.get(i))
#             d1[i]=d.get(i)
#     return d1

# d = {1: 10, 2: 20, 3: 30,4:90,5:56,6:56,7:100}
# print(dupli(d))

# 25. Write a program to check whether all values in a dictionary are unique.
# def unique(d):
#     l=[]
#     for i in d:
#         if d.get(i) not in l:
#             l.append(d.get(i))
#         else:
#             return "not unique"
#     return "unique"
# d={1: 10, 2: 20, 3: 30,4:90,5:56,6:57,7:100}
# print(unique(d))





