#Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second. 

num1 = int(input("Please enter the 1st number: "))

num2 = int(input("Please enter the 2nd number: "))

if num1 > num2:
    print(num2,'\n',num1)

elif num1 < num2:
    print(num1,'\n',num2)

else:
    print("They are equal")