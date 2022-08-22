#A rectangular living room has some number of doors and windows. A window has an area of 3
#square meters and a door has an area of 1.5 square meters. A One-liter tin of paint, which costs
#Rs 650/= will cover 25 square meters of wall. You are required to know the total area available
#to paint as well as the total cost of paint. You have the measurements of the height, length and
#width of the room in meters as well as the number of doors and windows. Write a computer
#program to solve this problem.

print("_________Painting Helper_________")
numberOfWindows=int(input("Enter Number of Windows \t: "))
numberOfDoors=int(input("Enter Number of Doors \t: "))
roomHeight=float(input("Enter Height of the Room \t "))
roomWidth =float(input("Enter Width of the Room \t "))
roomLength =float(input("Enter Length of the Room \t "))

areaOfWalls=roomHeight*roomWidth*roomLength
areaOfWindows=numberOfWindows*3
areaOfDoors=numberOfDoors*1.5

totalPaintingArea=areaOfWalls-areaOfWindows-areaOfDoors

if totalPaintingArea<0:
    print("Area of the Doors and Windows greater than the Walls")
else:
    print("Total Painting Area \t: {0:0.2f}".format(totalPaintingArea) )
    print("Total Cost for Panting \t: {0:0.2f}LKR".format(totalPaintingArea/650) )