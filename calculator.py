input_1=input("Enter the first number: ")
input_2=input("Enter the second number: ")
operation=input("Enter the operation: ")

if operation=="+": 
    print("The result is: ", int(input_1)+int(input_2))
elif operation=="-":
    print("The result is: ", int(input_1)-int(input_2))
elif operation=="*":
    print("The result is: ", int(input_1)*int(input_2))
elif operation=="/":
    print("The result is: ", int(input_1)/int(input_2))
else:
    print("Invalid operation")
    
    