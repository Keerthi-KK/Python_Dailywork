#Program to print factorial of given number
number=int(input("enter the numeric to get factorial of :"))
if number==1:
    print(f"factorial of {number}:",1)
elif number>0:
    
    factorial=1           
    for i in range(number,1,-1):
        factorial*=i
    print(f"factorial of {number} is {factorial}")

else:
    print("cannot find factorial for -ve numbers")
