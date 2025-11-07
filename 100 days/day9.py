# Day 9 --
# Armstrong NUmber
num=int(input("Enter number "))
temp =num
order = len(str(num))
total=0
while temp>0:
    digit=temp%10
    total+=digit**order
    temp//=10
if total==num:
    print("Armstrong number ")
else:
    print("Not armstrong number ")
