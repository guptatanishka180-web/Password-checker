#PYTHON PROGRAM TO CREATE A SIMPLE CALCULATOR
#Function to add to numbers

def add(num1,num2):    
    return num1 + num2

#function to substract two numbers
def sub(num1,num2):
    return num1 - num2

#function to divide two numbers
def divide(num1 , num2):
    return num1 / num2


#function to multiply two numbers
def multiply(num1 , num2):
    return num1 * num2

#function to average two numbers
def avg(num1 , num2):
    return (num1 + num2)/2


#STEP 2 : USER INPUT
print("please select a operation : \n " \
      "1. Addition\n" \
        "2. Substraction\n" \
            "3. Multiplication\n" \
            "4. Division\n" \
                   "5. Average\n")

select = int(input("Select a operation from 1,2,3,4,5:"))

number1 = int(input("enter first number : "))
number2 = int(input("enter second number : "))

#Step 3 : Print the result

if select == 1:
    print("sum of two numbers is : " , add(number1 , number2))


elif select == 2:
    print("substraction of two numbers is : " , sub(number1 , number2))


elif select == 3:
    print("multiply of two numbers is : " , multiply(number1 , number2))
    
    
elif select == 4:
    print("division of two numbers is : " , divide(number1 , number2))
    
elif select == 5:
    print("average of two numbers is : " , avg(number1 , number2))

else:
    print("invalid")


 
    