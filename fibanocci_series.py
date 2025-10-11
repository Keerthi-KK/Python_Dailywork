#fibanocci series
num=int(input("Enter no of terms:"))
first =0
last=1
print(first)
print(last)
for i in range(0,num):
        ans=first+last
        print(ans)
        first=last
        last=ans
