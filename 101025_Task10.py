#program to count no of even and odd numbers
end_digit=int(input("Enter the end number : "))

even=0
odd=0

for i in range(end_digit):
        if i%2==0:
              even+=1
        else:  odd+=1

print("No. of even numbers: ",even)
print("No. of odd numbers: ",odd)
