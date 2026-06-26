#-------dictionary---------
#Defination and property of dictionary
#creation of dictionary
#indexing and slicing.❌
#TRaversing
#in-built methods
#list comprehension
#Assignment and class activity

#------------Defination and property of dictionary.
#1.Dictionary is a data structure in python used store multiple data in #key:value format.
#2.ordered,mutable
#3. Indexed by key,not position.
#4.key must be unique(immutable)
#5.value can be any type of data.
#6. Uesd in Fast lookup.

#-----creation of dictionary.
# stu_profile={"aman":"noida","rohan":"delhi"}
# print(type(stu_profile))
# print(stu_profile)

# stu_marks=dict([('aman',300),("shivam",80)])
# print(stu_marks)

# stu_profile={"aman":"noida","rohan":"delhi"}
# stu_profile['aman']="delhi"
# print(stu_profile)

#inbulit-methods
# stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}
# v=stu_marks.values()
# k=stu_marks.keys()
# i=stu_marks.items()
# res=stu_marks.get('ruhi',"N/A")
# print(v)
# print(k)
# print(i)
# print(res)

#update()
# stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}
# new_marks={"kamal":89,"ram":77,"aman":30}
# stu_marks.update(new_marks)
# print(stu_marks)

profile={
  'aman':{
    'address':["Noida","Delhi","Mumbai"],
    'hobbies':["reading","cooking","travelling"],
    'password':{"insta":443345,"fb":678934},
  },
  'dev':{
    'address':["Noida","Delhi","Varanasi"],
    'hobbies':["reading","travelling","exploring","scubadiving"],
    'password':{"insta":333213,"fb":123456},
  }
}
print(profile['aman']['address'])
print(profile['dev']['hobbies'])
