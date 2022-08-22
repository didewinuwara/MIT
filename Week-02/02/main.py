#Using appropriate variables write a program to compute the area of a circle. You may try to
#enhance your program to compute:
#• both circumference and area
#• either circumference or area

import math

radius = float(input("Enter radius of the circle \t:"))
print("You can see bellow answers\n• Circumference - C \n• Area - A \n• Both -B")
choice = input("Press Letter related to your choice \t:")
try:
    circumference = round(2*math.pi*radius,2)
    area = round(math.pi*(radius**2,2))
    if (choice == 'C' or  choice=='c'):
        print("Circumference is :", circumference)

    elif (choice == 'A' or  choice=='a'):
        print("Area is :", area)

    elif (choice == 'B' or  choice=='b'):
        print("Area is :", area)
        print("Circumference is :", circumference)
except:
    print("_________Invalid_________")