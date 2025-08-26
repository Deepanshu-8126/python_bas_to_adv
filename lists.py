# Lists in Python
#1. What is a List?
# A list is an ordered, changeable (mutable) collection of items.
#
# Can hold different types (int, float, string, even another list).
# my_list = [10, "hello", 3.14, [1, 2, 3]]
# print(my_list) #print any lists

# acessing  lists elements
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])   # apple
# print(fruits[-1])  # cherry
# print(fruits[-2]) # banana

# Create a movie list and print first and last movie name
# my_movies = ["Bahubali", "Saiyarra", "Bahubali 2", "Suri", "Yodha"]
# print(my_movies[0])
# print(my_movies[-1])

# nums = [1, 2, 3, 4, 5]
# print(nums[1:4])   # [2, 3, 4]
# print(nums[::2])   # [1, 3, 5]
#Update
'''movies = ["Bahubali", "Saiyarra", "Bahubali 2", "Suri", "Yodha"]
movies.append("ice cream")
movies.remove("Saiyarra")
movies.pop()
movies.insert(2,"Bhaiyara")
movies.sort()
for i in movies:
    print(i)'''

#-------------------------------------------------------------------------------------

# Questionn ---ek list ka sum nikal (e.g. [1,2,3,4,5] → 15).
'''list = [1,2,3,4,5] # Builtt in function
sum =sum(list)
print(sum)'''

# 2-- Methoddd
'''list = [2,4,5,6,7]
total = 0
for num in list:
    total = total + num
print("Sum is :", total)'''

# Questionn 2 -- Maximum element find in a list
'''numbers = [5, 9, 2, 7, 3]

max_val = numbers[0] # First element assume 0 
for num in numbers:
    if num > max_val:
        max_val = num

print("Maximum element hai:", max_val)'''

# while loop
numbers = [5, 9, 2, 7, 3]
max_val = numbers[0]
while numbers>=max_val:
    print("Maximum element hai:", max_val)





