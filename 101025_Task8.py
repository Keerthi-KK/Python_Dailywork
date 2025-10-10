#program to print the harmonic series for given number and its sum
number=int(input("enter any number to print its harmonic series"))
sum=0

for i in range (1,(number+1)):
    print(f"1/{i}")
    sum+=1/i
print("Sum= ",sum)
