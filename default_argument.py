# x = 100   # global variable
#
# def show():
#     print("Inside function:", x)
#
# show()
# print("Outside function:", x)
 # Enclosing scope
# def outer():
#     x = "outer"
#
#     def inner():
#         print("Inner sees:", x)  # inner ko outer ka variable mil jaata hai
#
#     inner()
#
# outer()


# Non local keyword
def outer():
    x = "old"

    def inner():
        nonlocal x
        x = "new"

    inner()
    print("Outer sees:", x)


outer()
