#Arithmetic operations:
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=20
d=c+a
print(d)
print(f"a+b={a+b}")
print(f"a-b={a-b}")
print(f"a/b={a/b}")
print(f"a*b={a*b}")
print(F"c*b={c*b}")


print("select operations \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
option=int(input("enter choice"))
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))

if option==1:
    print(f"Addition:{a+b}")
elif option==2:
    print(f"Subtraction:{a-b}")
elif option==3:
    print(f"Multiplication:{a*b}")
elif option== 4:
    if b != 0:
        print(f"Division: {a / b}")
    else:
        print("Division by zero not allowed!")
else:
    print("Invalid choice!")
