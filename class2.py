# # to swap two variables
# a=10
# b=20

# print(a,b)

# # a,b=b,a

# # a=a+b
# # b=b-a
# # a=b-a


# print(a,b)
# to generate a random number
# import random
# print(random.random())
# print(random.randrange(1,100))

# to print largest

# a=20
# b=10
# c=20
# if((a>b and a>c) or (a==b and a>c) or (a==c and a>b)):
#     print("a is greater")

# elif((b>a and b>c) or (b==a and b>c) or (b==c and b>a)):
#     print("b is greater")

# elif((c>a and c>b) or (c==b and c>a)or (c==a and c>b)):
#     print("c is greater")

# else:
#     print("All numbers are equal")

# to print prime numbers in an interval

# for no in range(1,21):
#     for i in range(2, no):
#         if(no%i==0):
#             break
#         if (i == no - 1):
#             print(no)


#to print fibonacci numbers
# num=input("enter no of terms")
# count=0
# a=0
# b=1
# if(num<=0):
#    print("Not possible")
# elif(num==1):
#    print("fibonacci series upto", num)
#    print(a)
# else:
#    while(count<num):
#       print(a)
#       num=a+b
#       a=b
#       b=num
#       count+=1

#to iterate over dictionaries using for loop

# dt={'Name': 'zayns', 'Email':'zayn@gmail.com'}
# for key,value in dt.items():
#     print(key,value)

# #to count occurences in a list

# lt=['tripti', '7','10','tripti']
# occ=lt.count('tripti')
# print(occ)

# #to reverse a number
# number=537
# rev_num=0
# while(number!=0):
#     rem=number%10
#     rev_num=rev_num*10+rem
#     number//=10

# print("reversed number is :"+ str(rev_num))

#to count the number of digits present in a number

# number=456789
# count=0

# while(number!=0):
#     number//=10
#     count+=1

# print("Number of digits: " + str(count))

# #to remove whitespaces

# str="  Hello , I am zayn "
# print(str.strip())
#rstrip -right strip lstrip- left strip
# #to remove duplicates from an element

# testlist=['1','7','9','4','7','9','9','8']
# # print("The original list is: " + str(testlist))
# testlist2=list(set(testlist))
# print("After removing duplicates , list is", testlist2)


#to flatten  a nested list
# a=[1,2,3,4,5,[7,8,9],[9,4,5,7,9]]
# for idx in range(len(a)-1,0,-1):
#     if type(a[idx])== list:
#         a.extend(a[idx])#we use extend so that elements are added if we want to add the list we us eappend
#         a.pop(idx)

# print(a)


#to iterate two lists in parallel
# list1=[10,20,30,40,50]
# list2=[1,2,3,4,5]
# for idx in range(min(len(list1),len(list2))):
#     print(list1[idx],list2[idx])

#type vs instance (object of a type)
# a='10'
# b=None
# print(type(a),type(b))
# print(isinstance(b,str)) #gives true if s is string

# name ="mahesh"
# #string ="my name is %s this is my class."%name
# #string ="my name is {}.this is my class.".%s


#DUNCTIONS IN PYTHON

#def func_name(arg1,arg2,....)

#args-arguments
#kwargs- key word arguemnts+













#def func_name(key,calure,*args,**kwargs):
# print(key,value)
# print(args)
# print(kargs)


#functions can be nested inside each other


#first value is checked inside the function- local scope
#if nto found checked outside the function-global scope
#if function is defined inside fucntion , when value is not found in the second function but found in one function then it is called non local function

#import builtins as n/ import numpy as no
# from builtins import *(all functions)n/ from builtins import function_name(if not whole module only one function we want to import)

# Exception Handling: code ko try aur expect ke bichmei rkhte Handling
# try-run this code
# except-run this code if an exception occurs
# else- run this if no exception occurs
# finally- always run this code

# exception-value error
