print("calculator app")
num1=int(input("Enter Your First number: "))
num2=int(input("Enter Your Second number: "))
operator=input("Which Operator you use +,-,*,/,% : ")
if operator=="+":
    print(f" Addition of {num1} and {num2} are = {num1+num2}")
elif operator=="-":
       print(f" Subtraction of {num1} and {num2} are = {num1-num2}")
elif operator=="*":
       print(f" Multiplication of {num1} and {num2} are = {num1*num2}")
elif operator=="/":
      print(f" Division of {num1} and {num2} are = {num1/num2}")
elif operator=="%":
       print(f" Modulus of {num1} and {num2} are = {num1%num2}")
else:
    print("Enter Your Correct Operator")