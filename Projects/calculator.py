a = input("Enter operation do you want perform + - * % // :")
num_1 = int(input("Enter first number :"))
num_2 = int(input("Enter second number :"))

if a == "+":
    print(f"Addition of {num_1}+{num_2} is = {num_1+num_2}")
elif a == "-":
    print(f"Addition of {num_1}-{num_2} is = {num_1-num_2}")
elif a == "*":
    print(f"Addition of {num_1}%{num_2} is = {num_1 % num_2}")
elif  a == "%":
    print(f"Addition of {num_1}//{num_2} is = {num_1 // num_2}")
else:
    print(f"{a}Operator is  not valid")