#Task 4:Day2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Remainder:", num1 % num2)
print("Floor Division:", num1 // num2)


num = int(input("\nEnter a number: "))
num += 5
print("After incrementing by 5:", num)


num = int(input("\nEnter a number: "))
result = num * 3
if result >50: print("Triple value:", result)
else: print("result is less than 50")



# print True if both are greater than 10 using 'and'
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("Both greater than 10:", (a > 10) and (b > 10))


#  print True if at least one is greater than 10 using 'or'
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("At least one greater than 10:", (a > 10) or (b > 10))
