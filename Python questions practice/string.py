# count all vowels occurence
"""string=input("Enter string")
vowels="aeiou"
count=0
for i in string:
    if i in vowels:
        count+=1
print(count)
"""
"""# frequency check 
string=input("Enter string")
occ={}
for i in string:
    if i in occ:
        occ[i]+=1
    else:
        occ[i]=1
print(occ)"""

# anagram number check listen - silent
# same frequency same letters
# sort method
"""string=input("Enter number")
string_1=input("Enter string")
if sorted(string)==sorted(string_1):
    print("Anagram")
else:
    print("Not anagram")
"""

# Question -- Count frequency of a particular character eg l
"""string=input("Enter string")
target="l"
count=0
for i in string:
    if i==target:
        count+=1
print(count)
"""

# Question -- count how many words are in a sentence
"""text = "Python is very easy"
count=0
for i in text:
    if i in text:
        count+=1
print(count) # space also count

text = "Python is very easy"
split_1=text.split()
count=0
for i in split_1:
    if i in split_1:
        count+=1
print(count)
"""
