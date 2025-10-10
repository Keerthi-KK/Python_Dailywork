#program to find number and count of all divisble by 9 between 100 -200

sum=0
count=0

for i in range(100,201):
    if i %9==0:
        print(i)
        sum+=i
        count+=1
print("Count of numbers divisible by 9 between 100-200 are :",count)
print("Sum of numbers divisible by 9 between the range is :",sum)
