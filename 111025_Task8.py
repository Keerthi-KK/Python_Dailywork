#Sum of Matrix Elements
sum=0
for i in range(1,3):
    for j in range(1,3):
        print(i*j, end=" ")
        sum+=(i*j)
    print()
print(sum)
