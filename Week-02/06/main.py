#Further to the above problem in Q5, suppose you as the contractor are supposed to issue a bill
#to the customer which contains the material cost, labor cost, the transport cost and the total
#cost. Write a computer program to display the bill on screen. You can input the labor cost and
#transport cost.

#Note: A bill typically includes some additional data such as the contractors name and address,
#bill issued date, who created the bill, any discounts, etc.

import random

def materialCostCalc():
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
        materialCostCalc()
    else:
        return totalPaintingArea


materialCost=materialCostCalc()
labourCost=float(input("Enter labour cost \t: "))
transportCost=float(input("Enter transport cost \t: "))
totalCost= materialCost+labourCost+transportCost

orderNumber = random.randint(0,100000)

print("\n-------ABC Hardware---------")
print("______________________________")
print("No: 300/E, main Street, Galle.")
print("______________________________")
print("Cashier:Dhanushka")
print("Order Number:%s\n"%orderNumber)
print("______________________________")
print("Material Cost\t:%s"%materialCost)
print("Labour Cost\t:%s"%labourCost)
print("Transport Cost\t:%s"%transportCost)
print("______________________________")
print("\nTotal Cost\t:%s"%totalCost)
print("______________________________")
print("___Thank you for your visit___")
