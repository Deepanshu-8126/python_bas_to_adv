#----------------------Day 1--------------------------------------
# Problem -- Write a Python Program to reverse a string  -- without using [::-1]
text = "DkDropz"
reversed_text="" # empty string
for ch in text:
    reversed_text=ch+ reversed_text
print(reversed_text)

text = input("Enter text")
rev=""
for char in text:
    rev = char+rev
print(rev)