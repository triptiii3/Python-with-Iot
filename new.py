#CALCULATOR

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def divisor(x,y):
    return x%y


#PASSWORD GENERATOR
import random
import string
first=string.ascii_lowercase
second=string.ascii_uppercase
third=string.digits

characters=first+second+third
password = ''.join(random.choice(characters) for i in range(8))

print(password)


