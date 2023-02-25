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

