# format specifiers
# colon add : this colon are called format specifiers
price1 =3.14159
price2=-987.65
price3=12.34

'''print(f"Price 1 is {price1:.2f}") # 3.14159 to 3.14
print(f"Price 2 is {price2:.1f}") #987.65 to 987.6
print(f"Price 3 is {price3:.1f}") # 12.3

# .3f will show three decimal places
print(f"Price 1 is {price1:.3f}") #3.142'''

 # Each value has 10 line spaces
'''print(f"Price 1 is {price1:.10}")
print(f"Price 2 is {price2:.10}")
print(f"Price 3 is {price3:.10}")'''

# each number withh paded with 0 in empty
'''price1 =3.14159
price2=-987.65
price3=12.34
print(f"Price 1 is ${price1:.010}") #000$31.4159
print(f"Price 2 is ${price2:.010}")
print(f"Price 3 is ${price3:.010}")'''

'''print(f"price 1 is {price1:+}") #+3.14159'''
# , comma will separate


'''print(f"Price 1 is ${price1:+,.2f}") #000$31.4159
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")'''