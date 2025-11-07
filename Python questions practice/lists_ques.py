# Find largest number inn list
"""list = [10,20,30,40]
max = max(list)
print(max) #builtin function
print(min)"""


# Reverse lists
'''lists = [10,20,30,40]
reversed_lists=lists[::-1]
print("Reversed lists :", reversed_lists)'''
'''this_lists = [10,20,30,40]
this_lists.reverse()
print(this_lists)'''

# ANOTHER METHOD
'''this_lists.sort(reverse=True)
print(this_lists)
'''

# Take 5 numbers from user, store in a list, print:
#  SumAverage Max Min
'''lists =[]
for i in range(5):
    n =int(input("Enter any number"))
    lists.append(n)
print("List:", lists)
print("Sum:", sum(lists))
print("Avg:", sum(lists)/5)
print("Max:", max(lists))
print("Min:", min(lists))'''

# Question 2: Remove duplicates from a list using a set
'''lists=[1,1,2,3,4,5]
duplicate_remove= list(set(lists))
print(duplicate_remove)'''

#Swap first and last element of a list
'''lists = [2,3,4,5,6,7]
lists[0],lists[-1]=lists[-1],lists[0]
print(lists) '''
#Count how many times each word appears in a list.
'''lists = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(lists.count('apple'))'''

#Tuples
#Store student records as tuples: (name, age, grade)
# merge two lists
# Merge two lists
'''list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3= list1+list2
print(list3)'''


# Remove specific elements by value and index
'''numbers = [1, 2, 3, 2, 4, 2, 5]
# Remove all occurrences of 2
print(list(set(numbers)))
remove= list(set(numbers))'''
# Check if an element exists in list
'''names = ['Alice', 'Bob', 'Charlie']
# Check if 'Bob' exists
if 'Bob' in names:
    print("Yes bob in names")
else:
    print('Bob in not in names')'''
# Calculate sum of all numbers in list
'''numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(total)'''

# 13. Remove duplicates
'''numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
'''
# Find maximum numbers in list
'''scores = [85, 92, 78, 96, 88]
max_score = scores[0] # assume first scores is max
for score in scores:
    if score > max_score:
        max_score=score

print(max_score)
'''

# Question -- minimun in the list
'''scores = [85, 92, 78, 96, 88]
min_score=scores[0]
for score in scores:
    if score<min_score:
        min_score = score
        print(score)
'''

# Second largest number find in a list
# first method
'''numbers = [85, 92, 78, 96, 88]
#initialise first
first_num = numbers[0]
second_num = numbers[0]

#loop for first num
for num in numbers:
    if num>first_num:
     first_num= num

# Second largest
for num in numbers:
    if num>second_num and num<first_num:
        second_num= num

print("First largest number :", first_num)
print("Second largest number :", second_num)
'''
'''
# Second Method sort
numbers = [85, 92, 78, 96, 88]
sorted_numbers = sorted(numbers, reverse=True)
first_largest = sorted_numbers[0]    # 96
second_largest = sorted_numbers[1]   # 92

print("Second Largest:", second_largest)'''

# Even list make for another list
'''lists = [1,2,4,5,6,8,22,44,66,63,54]
even_no=[]
for num in lists:
    if num%2==0:
      even_no.append(num)
      print(f"Even number is {even_no}")'''
#odd numbers
'''lists = [1,2,4,5,6,8,22,44,66,63,54]
odd_no =[]
for num in lists:
    if num%2!=0:
     odd_no.append(num)
    print(f"Odd numberss is :{odd_no}")
    
'''
# list avergae nikalna average = total sum + total numbers
'''lists = [1,2,3,4,5,6]
total_numm =0
for num in lists:
    total_numm=total_numm+num
#Average
average= total_numm/len(lists)
print("Sum is :", total_numm)
print("Average is :", average)

'''
# largest three numbers
'''numbers = [10, 5, 8, 20, 15, 25, 3]
sorted_numbers = sorted(numbers, reverse=True)
largest_three = sorted_numbers[:3]
print(largest_three)'''

# find duplicate numbers in list
'''List=[1,1,2,3,4,5,6,7,3,5,2]
new_list = []
for i in List:
    if i not in new_list:
        new_list.append(i)
print(new_list)'''

"""'''# count method
numbers=[1,1,2,3,4,4,5,5,6,6]
duplicates=[]

for i in numbers:
     if numbers.count(i)  >1  and i not in duplicates:
      duplicates.append(i)

print("Original value :", numbers)
print("Duplicate value :", duplicates)'''"""

# Count how many even numbers in a list
"""list_=[1,2,3,4,5,6,66,8,88]
count=0
for i in list_:
    if i%2==0:
        count+=1
print(count)

# filter out
filter_even=list[list%2==0]
print(filter_even)"""

"""# find duplicates from a list
list=[1,2,1,34,4,5,5,6,7,8]
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print("Original list",list)
print("New list",new_list)"""


# USER INPUT 5 INTGER NUMBERS FIND MINIMUM
"""l=[]
for i in range(5):
    number=int(input("Enter number"))
    l.append(number)
print("Minimum number ",min(l))
"""

