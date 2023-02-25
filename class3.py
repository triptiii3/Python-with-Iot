#FUNCTIONS IN PYTHON

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
import new

print("Select your operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Divisor")
try:
   choice = str(input("Enter the operation (1,2,3,4,5): "))
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))


   if choice == '1':

        print("num1", "+", "num2", "=", new.add(num1, num2))
   elif choice == '2':
        print("num1", "-", "num2", "=", new.subtract(num1, num2))
   elif choice == '3':
        print("num1", "X", "num2", "=", new.multiply(num1, num2))
   elif choice == '4':
        print("num1", "/", "num2", "=", new.divide(num1, num2))
   elif choice == '5':
        print("num1", "%", "num2", "=", new.divisor(num1, num2))
except Exception as e:
    print("exception occured: ", e)
else:
    print("code execution successful")
finally:
     print("Code executed.")

