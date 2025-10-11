
#program to print alphabet triangle pattern
alpha=["A","B","C","D"]
for i in range(0, 4):
    for j in range( i + 1):
        print(alpha[j], end="")
    print()
