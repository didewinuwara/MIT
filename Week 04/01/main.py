# find the maximum mark related to 10 students

def findAvg(markList):
    total=0
    for i in markList:
        total+=i
    print("Average is \t:",total/(len(markList)))

def findMax(markList):
    maximum=markList[0]
    minimum=markList[0]
    markList.pop(0)
    for i in markList:
        if maximum<i:
            maximum=i
        if minimum>i:
            minimum=1
    print('maximum is \t:',maximum)
    print('minimum is \t:',minimum)

markList=[]
for count in range(10):
    mark=float(input("Enter Marks :"))
    markList.append(mark)
# if you have student mark list above 21-23 lines not nessasary  

findAvg(markList)
findMax(markList)
#otherwise we can use max function 