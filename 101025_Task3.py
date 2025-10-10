#Program to print first 10 Natural Numbers and their sum 
sum=0
number=int(input("Enter end number: "))
for i in range(1,(number+1)):
    sum+=i
    print(i)
print(f"sum of first {number}  Natural numbers=",sum)
    
