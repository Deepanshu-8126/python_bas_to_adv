# day 14 ---  python series ---

for row in range(6):
    for col in range(7):
        # Logic to print stars in a Heart shape
        if (row == 0 and col % 3 != 0) or \
           (row == 1 and col % 3 == 0) or \
           (row - col == 2) or \
           (row + col == 8):
            print("❤️", end=" ")
        else:
            print("  ", end=" ")
    print()

print("Hello World i am deepanshu ")

