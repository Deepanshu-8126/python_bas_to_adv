# --------------------DAy2--
#Problem-- count all the vowels in a string
text = "DkDropzPython"
vowels = "aeiouAeiou"
count = 0
for ch in text:
    if ch in vowels:
        count+=1
print(count)