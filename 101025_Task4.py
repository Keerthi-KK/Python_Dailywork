#Program to print first 10 Natural Numbers and find their sum,average
sum=0
number=10
for i in range(1,(number+1)):
    sum+=i
    print(i)
avg=sum/number
print(f"sum of first {number}  Natural numbers=",sum)
print(f"Average of first {number}  Natural numbers=",avg)


