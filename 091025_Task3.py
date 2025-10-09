#Get two values from user and type
# a for + Addition
#b for - subtraction
#c for * Multiplication
#d for / Division


num1=int(input("Enter value 1: "))
num2=int(input("Enter value 2: "))

print("Options for Operations are:")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
type=input("Enter any option")
if type=="a":
         print("a+b=",num1+num2)
elif  type=="b":
         print("a-b=",num1-num2)
elif  type=="c":
         print("a*b=",num1*num2)
elif  type=="d":
    if num2>0:
                 print("a/b=",num1/num2)
    else: print("cannot divide by 0")
else: print("Enter a valid option")


         
