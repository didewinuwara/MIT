print("\t Madhumal Motors")
print("---------No:36, Kaduwela---------")
print("_________________________________")

#define inventory
inventory = []

while True:
    #menu
    print("1. Add a Bike\n2. Search price for a bike \n3. Create a Invoice \n4. Display Inventory Report\n")

    #get user choice
    choice = int(input("Enter your selection : "))

    #if user need to add a details
    if choice == 1:
        make=input("Enter Bike make \t:")
        model=input("Enter Bike Modal \t:")
        quantity=input("Enter Bike Quantity \t:")
        price=input("Enter Bike price \t:")
        record=[make,model,quantity,price]
        inventory.append(record)
        print("\n--successfully added ---\n")

    #if user need to create a invoice
    elif choice ==2:
        make=input("Enter Bike make \t:")
        model=input("Enter Bike Modal \t:")
        #search product
        for record in inventory:
            availability=False
            if record[0]==make and record [1]==model:
                availability=True
                print ("Company- %s \tModal- %s \tprice - %s" %(record[0],record[1],record[3]))
            else :
                availability=False
                
        if availability==False:
            print("Product Doesn't exist ")

    #if user need to create a invoice
    elif choice ==3:
        make=input("Enter Bike make \t:")
        model=input("Enter Bike Modal \t:")
        quantity=int(input("Enter Bike Quantity \t:"))
        for record in inventory:
            availability=False
            #check the product availibility
            if record[0]==make and record [1]==model:
                #check the quantity availibility 
                if (int(record[2]))>=quantity:
                    availability=True
                    record[2]=int(record[2])-quantity
                    print("\n\t Madhumal Moters")
                    print("---------No:36, Kaduwela---------\n")
                    print("_________________________________\n")
                    print("-------------Invoice-------------\n")
                    print("%s \t %s\t %s\t %s"%(record[0],record[1],quantity,float(record[3])*quantity))
                    print("_________________________________\n")
                    print("Total\t\t\t%s"%(float(record[3])*quantity))
                    print("_________________________________\n")
                    print("\tThank you\n")
                else:
                    availability=False
            else:
                availability=False
        if availability==False:
            print("Product or Quantity Doesn't exist ")

    #if user need to see the inventory
    elif choice ==4:
        print ("-------------Inventory-------------\n")
        for record in inventory:
            print("%s \t %s\t %s\t %s"%(record[0],record[1],record[2],record[3]))
    else:
      print("Invalid Number")
                
    #Check the continuity of the programme
    continuePrograme=input("Do you need to continue this, press 'y/n' :")
    if continuePrograme == 'y' or continuePrograme == 'Y':
        continue
    elif continuePrograme == 'n' or continuePrograme == 'N':
        break
    else:
        print("Wrong Input, Process will start again")
    
