#program to find numbers divisible by 7 and multiple of 5 between 1 -100 (both included)

for i in range(1,101):
    if i%7==0 and i%5==0:
        print(i)
        
