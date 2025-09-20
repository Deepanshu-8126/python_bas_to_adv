# Aggregation -- has an relationship library book car engine
# Book class
"""class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")


# Library class (Aggregation -> has-a relationship)
class Library:
    def __init__(self, books):
        self.books = books   # yaha Book objects ki list aa rahi hai

    def show_library_books(self):
        print("Library has the following books:")
        for book in self.books:
            book.show_details()   # Book ka method call ho raha hai


# Objects of Book
b1 = Book("Python Basics", "Guido van Rossum", 500)
b2 = Book("Learning Java", "James Gosling", 400)
b3 = Book("C++ Primer", "Bjarne Stroustrup", 600)

# Library object banate waqt Book objects pass kar diye
library = Library([b1, b2, b3])

# Show all books in library
library.show_library_books()"""
# college - department aggregation department independt
#ggregation me Department ek independent class hoga (jaise BCA, BBA
# alag–alag departments) aur College ek dusra class hoga jiske andar
# ye departments honge.
# 📌 So structure kuch aisa hoga:
# Department class → dept_name, HOD
# College class → apne pass ek list of departments rakhega
"""class Department:
    def __init__(self,dept_name,hod):
        self.dept_name=dept_name
        self.hod=hod
    def show_details(self):
        print(f"Department name is :{self.dept_name}, and Hod is  :{self.hod}")
class College:
    def __init__(self,departments):
        self.departments=departments
    def show_departments(self):
        for depart in self.departments:
            depart.show_details()

#object
d1=Department("BBa","Ayushi")
d2=Department("bca","Hema negi")
d3=Department("Paramdeical","k")

college = College([d1, d2, d3])
college.show_departments()
#College ke andar multiple Department objects ka collection aa gaya,
# aur wo independent bhi exist karte hain.College ke
# andar multiple Department objects ka collection aa gaya
# , aur wo independent bhi exist karte hain."""

# Q4. Team–Players
#
# Ek Team class aur ek Player class banao. Team ke andar multiple players hote hain.
# Team ke object ke through sab players ka data show karna hai.
"""class Player:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def show(self):
        print(f"Player name is {self.name} and age is {self.age}")
class Team: 9
    def __init__(self,players):
        self.players=players
    def show_player_details(self):
        for player in self.players:
            player.show()  #player method call
# object create
p1=Player("Deepanshu",19)
p2=Player("Vishal",19)
p3=Player("Himanshu",19)
p4=Player("Sandy",19)
p5=Player("Gaurav Goswami",19)

team =Team([p1,p2,p3,p4,p5])
team.show_player_details()
# team mutiple players ko represent kr rahi hey so list banayi team=Team(p1)"""