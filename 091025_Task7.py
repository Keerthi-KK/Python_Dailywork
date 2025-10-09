# Program to check whether the given rectangle is a square or not

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if length > 0 and breadth > 0:
    if length == breadth:
        print("It is a Square.")
    else:
        print("It is a Rectangle.")
else:
    print("Length and Breadth should be positive values.")
