a=10
b=20
c=3
d=40
e=50
f=a/(d+e)-d*b**c
print(f)

a1=int(input("Enter a number you want to divide"))
a2=int(input("Enter the number you want to divide it with"))
if a1%a2==0:
    print("It is divisible")
else:
    print("It is not divisible")


mean=38
count=40
wrong_number=36
correct_number=56
sum=mean*count
print("The sum is",sum)
difference= correct_number-wrong_number
print('The difference is',difference)
new_sum= difference+sum
new_mean= new_sum/count
print("The correct mean is",new_mean)