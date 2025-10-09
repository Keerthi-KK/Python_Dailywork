#Program to check whether a triangle is Equilateral triangle ,Isoceles ,Scalene

side_A=int(input("Enter the value of  side A :"))
side_B=int(input("Enter the value of  side B :"))
side_C=int(input("Enter the value of  side C :"))
# Check condition for triangle sum of any 2 sides must be greater than 3 rd side

if (side_A + side_B>side_C ) and  (side_B+side_C>side_A) and (side_A+side_C>side_B):
    print("Its a valid triangle")
    if (side_A==side_B) and (side_B==side_C):
        print("Its is an  Equilateral Triangle")
    elif (side_A==side_B) or (side_B==side_C) or (side_B==side_A):
        print("Its is an Isoceles Triangle")
    else: print("It is a Scalene Triangle")
else:
    print("Not a valid triangle")
    
