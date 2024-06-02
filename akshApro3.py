num=int(input("enter a natural number:"))
sum=0
if num<=0:
    raise Exception("Enter a positive number")
else:
    for i in range(1,num+1):
        sum=sum+i
print(sum)
