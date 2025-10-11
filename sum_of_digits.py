#Sum of Digit
a=int(input("Enter the number"))
sum=0
for i in str(a):
    sum+=int(i)
print("sum of digits:",sum)
