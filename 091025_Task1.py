#Program to read the temperature in centigrade and display a msg according to the temperature

temp=int(input("Enter a temperature"))
if temp<=0 :
         print("freezing weather")
elif temp>0  and  temp <=10:
         print("Very cold Weather")
elif  temp>10 and temp <=20:
         print("Cold Weather")
elif temp >20 and temp <=30:
        print("Normal in temp")
elif temp >30 and temp<=40:
        print("Its Hot")
elif temp>=40 :
    print("Very Hot")
else:
    print("Invalid Temperature")
