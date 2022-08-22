#An employee works at the head office of a company in Colombo. The company has branches in
#Galle, Kandy, Matara, Katunayake and Ratnapura. There is an expressway entrance in Colombo
#from where, expressways run to all those cities. Distances from Colombo to those cities (in kms)
#are 110, 111, 150, 25, and 112 respectively. Write a computer program for the user to know the
#time it takes to go to a particular city from Colombo. (Note: You may ignore the traveling time
#outside expressways).

#Assumption
#-Average speed on the Highway -60km/h

def time(index):
    townDistanceList=[110,111,150,25,112]
    time= townDistanceList[index]/60

    seconds = time * 3600
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return ("%d:%02d:%02d (hh:mm:ss)" % (h, m, s))

print("_________Speed Table_________\n")
print("_________Town List_________")
print("•Galle -G \n•Kandy -K \n•Matara -M \n•Katunayaka -C \n•Ratnapura -R")
choice = input("Enter Your Destination : \t")

if (choice=='G' or choice =='g'):
    print ("Tour will take {0}".format(time(index=0)))
elif (choice=='K' or choice =='k'):
    print ("Tour will take {0}".format(time(index=1)))
elif (choice=='M' or choice =='m'):
    print ("Tour will take {0}".format(time(index=2)))
elif (choice=='C' or choice =='c'):
    print ("Tour will take {0}".format(time(index=3)))
elif (choice=='R' or choice =='r'):
    print ("Tour will take {0}".format(time(index=4)))
else:
    print("_________Invalid Input_________")


