#MATCH -case statements
#from calendar import TUESDAY

#
# def number_check(x):
#     match x:
#         case 1:
#             return "One"
#         case 2:
#             return "Two"
#         case 3:
#             return "Three"
#         case _:
#             return "Other number"
#
# print(number_check(1))   # One
# print(number_check(5))   # Other number

"""def day_of_week(day):
     match day:
         case 1:
             return "It is Sunday"
         case 2:
             return "It is MOnday"
         case _:
             return "not a valid day"
print(day_of_week(1))
print(day_of_week(2))
print(day_of_week(9))"""
from calendar import TUESDAY


"""def is_weekend(day):
    match day:
        case "Monday" |"Tuesday":
            print("False")
        case "Sunday" | "Saturday":
            print("Wekkend")




is_weekend("Monday")"""

'''def check_num(x):
    match(x):
        case x if x>0 :
            return "positive"
        case x if x<0:
            return "negative"



print(check_num(-3))'''

# Exercise 1--PRINT Write a Python program using match-case
# that prints the day of the week (1 → Monday, 7 → Sunday). If input is not 1–7, print "Invalid Day"

'''def _class_(*args,**kwargs):
    print(args)
    print(kwargs)
    for i in kwargs:
        print(kwargs[i])
    for j in args:
        print(j,end=",")

_class_("jjdfjhjf",2383,27838293,name="deepasnsjhu",age=18)'''

# def add_numbers(*args):
#     total = 0
#     for num in args:
#        total +=num
#     return total
# print(add_numbers(2,4,5,6))

# def sub_numbers(*args):
#     total=0
#     for num in args:
#         total -=num
#     return total
# print(add_numbers(2,3,4,45))
# def person_info(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     for i in kwargs:
#         print(i)
#     for j in args:
#         print(j)
# person_info("Rahul", 23, "threee", name = "Deepanshu", age =45,going =


"""
def fact(num):
    match num:
        case 1 :
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case _:
            return "Invalid Case"
print(fact(1))"""

def day_of_week(day):
    match day:
        case "Saturday" | "Sunday":
            print("IS Weekend")
        case "Monday"|"Wednesday":
            print("Work Day")
    print(day_of_week("Sunday"))